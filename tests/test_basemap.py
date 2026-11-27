import colorsys
import os
import tempfile
import time
import unittest
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
from io import BytesIO
from pathlib import Path
from unittest.mock import MagicMock, patch
from urllib.parse import parse_qs, urlparse

import requests
from PIL import Image

from simple_dwd_weatherforecast import basemap, dwdmap
from simple_dwd_weatherforecast.basemap import (
    BaseMap,
    BaseMapNotAvailableError,
    BaseMapStyle,
)

WIDTH = 200
HEIGHT = 100
SECTION = (9.0, 49.0, 10.0, 50.0)
LAND = (240, 230, 220)
RAIN = (0, 0, 255)
SLOT = datetime(2026, 11, 25, 21, 0, tzinfo=timezone.utc)


def png(color, size=(WIDTH, HEIGHT), mode="RGB"):
    buffer = BytesIO()
    Image.new(mode, size, color).save(buffer, format="PNG")
    return buffer.getvalue()


def response(content, status=200, content_type="image/png"):
    result = MagicMock()
    result.status_code = status
    result.content = content
    result.headers = {"content-type": content_type}
    if status >= 400:
        result.raise_for_status.side_effect = requests.HTTPError(str(status))
    return result


def weather_png():
    """Transparent weather image with rain in the upper left quarter."""
    image = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    image.paste((*RAIN, 255), (0, 0, WIDTH // 2, HEIGHT // 2))
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    return buffer.getvalue()


def new_basemap(**kwargs):
    return BaseMap(*SECTION, WIDTH, HEIGHT, **kwargs)


class BaseMapTestCase(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.cache_dir = directory.name
        patcher = patch("simple_dwd_weatherforecast.basemap.requests.get")
        self.get = patcher.start()
        self.addCleanup(patcher.stop)
        self.get.return_value = response(png(LAND))

    def cached_files(self):
        return list(Path(self.cache_dir).iterdir())

    def make_outdated(self):
        (path,) = self.cached_files()
        old = (datetime.now(timezone.utc) - timedelta(days=400)).timestamp()
        os.utime(path, (old, old))

    def test_request(self):
        new_basemap().get_image()
        url = urlparse(self.get.call_args.args[0])
        query = parse_qs(url.query)
        self.assertEqual(url.hostname, "sgx.geodatenzentrum.de")
        # WMS 1.3.0 with EPSG:4326 expects latitude first
        self.assertEqual(query["BBOX"], ["49.0,9.0,50.0,10.0"])
        self.assertEqual(query["WIDTH"], [str(WIDTH)])
        self.assertEqual(query["HEIGHT"], [str(HEIGHT)])
        self.assertIsNotNone(self.get.call_args.kwargs["timeout"])

    def test_downloaded_once(self):
        base = new_basemap()
        base.get_image()
        base.get_image()
        self.assertEqual(self.get.call_count, 1)

    def test_parallel_access_downloads_once(self):
        base = new_basemap()

        def slow(*_, **__):
            time.sleep(0.05)
            return response(png(LAND))

        self.get.side_effect = slow
        with ThreadPoolExecutor(8) as pool:
            list(pool.map(lambda _: base.get_image(), range(16)))
        self.assertEqual(self.get.call_count, 1)

    def test_no_files_without_cache_dir(self):
        new_basemap().get_image()
        self.assertEqual(self.cached_files(), [])

    def test_read_from_disk(self):
        new_basemap(cache_dir=self.cache_dir).get_image()
        image = new_basemap(cache_dir=self.cache_dir).get_image()
        self.assertEqual(self.get.call_count, 1)
        self.assertEqual(image.getpixel((0, 0)), (*LAND, 255))

    def test_cache_dir_is_created(self):
        directory = os.path.join(self.cache_dir, "new", "folder")
        new_basemap(cache_dir=directory).get_image()
        self.assertEqual(len(os.listdir(directory)), 1)

    def test_other_section_other_file(self):
        new_basemap(cache_dir=self.cache_dir).get_image()
        BaseMap(
            8.0, 49.0, 9.0, 50.0, WIDTH, HEIGHT, cache_dir=self.cache_dir
        ).get_image()
        self.assertEqual(self.get.call_count, 2)
        self.assertEqual(len(self.cached_files()), 2)

    def test_other_style_other_file(self):
        new_basemap(cache_dir=self.cache_dir).get_image()
        new_basemap(cache_dir=self.cache_dir, style=BaseMapStyle.DARK).get_image()
        self.assertEqual(len(self.cached_files()), 2)

    def test_unreadable_file_is_replaced(self):
        new_basemap(cache_dir=self.cache_dir).get_image()
        (path,) = self.cached_files()
        path.write_bytes(b"no image")
        image = new_basemap(cache_dir=self.cache_dir).get_image()
        self.assertEqual(image.getpixel((0, 0)), (*LAND, 255))
        self.assertEqual(self.get.call_count, 2)

    def test_outdated_file_is_refreshed(self):
        new_basemap(cache_dir=self.cache_dir).get_image()
        self.make_outdated()
        self.get.return_value = response(png((1, 2, 3)))
        image = new_basemap(cache_dir=self.cache_dir).get_image()
        self.assertEqual(image.getpixel((0, 0)), (1, 2, 3, 255))

    def test_outdated_file_is_kept_if_server_fails(self):
        new_basemap(cache_dir=self.cache_dir).get_image()
        self.make_outdated()
        self.get.side_effect = requests.ConnectionError
        base = new_basemap(cache_dir=self.cache_dir)
        image = base.get_image()
        base.get_image()
        self.assertEqual(image.getpixel((0, 0)), (*LAND, 255))
        # one download, one failed refresh, no further request
        self.assertEqual(self.get.call_count, 2)

    def test_image_in_memory_is_refreshed(self):
        base = new_basemap()
        base.get_image()
        base._loaded -= timedelta(days=400)
        base.get_image()
        self.assertEqual(self.get.call_count, 2)

    def test_not_available(self):
        self.get.side_effect = requests.ConnectionError
        base = new_basemap()
        for _ in range(3):
            with self.assertRaises(BaseMapNotAvailableError):
                base.get_image()
        self.assertFalse(base.available)
        self.assertEqual(self.get.call_count, 1)

    def test_retry_after_failure(self):
        self.get.side_effect = requests.ConnectionError
        base = new_basemap()
        self.assertFalse(base.available)
        self.get.side_effect = None
        base._retry_after = datetime.now(timezone.utc)
        self.assertTrue(base.available)

    def test_http_error(self):
        self.get.return_value = response(png(LAND), status=503)
        self.assertFalse(new_basemap().available)

    def test_service_exception_with_status_200(self):
        self.get.return_value = response(
            b"<ServiceException/>", content_type="text/xml"
        )
        self.assertFalse(new_basemap().available)

    def test_wrong_size(self):
        self.get.return_value = response(png(LAND, size=(10, 10)))
        self.assertFalse(new_basemap().available)

    def test_error_while_storing_is_ignored(self):
        with patch.object(Image.Image, "save", side_effect=OSError):
            self.assertTrue(new_basemap(cache_dir=self.cache_dir).available)

    def test_apply(self):
        weather = Image.open(BytesIO(weather_png()))
        image = new_basemap().apply(weather)
        self.assertEqual(image.mode, "RGB")
        self.assertEqual(image.size, (WIDTH, HEIGHT))
        self.assertEqual(image.getpixel((0, 0)), RAIN)
        self.assertEqual(image.getpixel((WIDTH - 1, 0)), LAND)

    def test_apply_does_not_change_the_basemap(self):
        base = new_basemap()
        base.apply(Image.open(BytesIO(weather_png())))
        self.assertEqual(base.get_image().getpixel((0, 0)), (*LAND, 255))

    def blend(self, land, weather, style=BaseMapStyle.LIGHT):
        self.get.return_value = response(png(land))
        base = new_basemap(style=style)
        image = Image.new("RGBA", (WIDTH, HEIGHT), weather)
        return base.apply(image, blend=True).getpixel((WIDTH - 1, 0))

    def test_blend_keeps_the_colors_on_white(self):
        self.assertEqual(self.blend((255, 255, 255), (51, 250, 10, 255)), (51, 250, 10))

    def test_blend_shows_dark_names(self):
        self.assertEqual(self.blend((0, 0, 0), (51, 250, 10, 255)), (0, 0, 0))

    def test_blend_on_dark_map(self):
        # white land becomes black on the dark map and black names become white
        dark = BaseMapStyle.DARK
        color = (51, 250, 10, 255)
        self.assertEqual(self.blend((255, 255, 255), color, dark), (51, 250, 10))
        self.assertEqual(self.blend((0, 0, 0), color, dark), (255, 255, 255))

    def test_blend_without_weather(self):
        self.assertEqual(self.blend(LAND, (0, 0, 0, 0)), LAND)

    def test_blend_respects_transparency(self):
        red, _, _ = self.blend((255, 255, 255), (55, 0, 0, 128))
        self.assertAlmostEqual(red, 155, delta=2)

    def test_blend_is_off_by_default(self):
        self.get.return_value = response(png((0, 0, 0)))
        image = new_basemap().apply(Image.open(BytesIO(weather_png())))
        self.assertEqual(image.getpixel((0, 0)), RAIN)

    def test_source_note_is_drawn(self):
        empty = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
        image = new_basemap().apply(empty)
        corner = image.crop((0, HEIGHT - 20, 100, HEIGHT))
        self.assertGreater(len(corner.getcolors(maxcolors=2000)), 2)

    def test_attribution(self):
        base = new_basemap()
        base.get_image()
        base._loaded = datetime(2024, 5, 1, tzinfo=timezone.utc)
        self.assertIn("© BKG (2024) dl-de/by-2-0", base.attribution)
        self.assertIn("https://sgx.geodatenzentrum.de/web_public", base.attribution)
        self.assertNotIn("verändert", base.attribution)

    def test_attribution_without_basemap(self):
        self.assertIn("© BKG (2025) dl-de/by-2-0,", basemap.attribution(year=2025))
        this_year = str(datetime.now(timezone.utc).year)
        self.assertIn(this_year, basemap.attribution(BaseMapStyle.DARK))
        self.assertIn("Daten verändert", basemap.attribution(BaseMapStyle.DARK))
        self.get.assert_not_called()

    def test_attribution_of_changed_map(self):
        base = new_basemap(style=BaseMapStyle.DARK)
        self.assertIn("Daten verändert", base.attribution)

    def test_dark_style(self):
        image = new_basemap(style=BaseMapStyle.DARK).get_image()
        self.assertLess(max(image.getpixel((0, 0))[:3]), 60)


class InvertLightnessTestCase(unittest.TestCase):
    def test_same_as_hls(self):
        for color in (
            (255, 255, 255),
            (0, 0, 0),
            (120, 180, 240),
            (240, 170, 90),
            (10, 200, 30),
            (90, 90, 90),
        ):
            hue, lightness, saturation = colorsys.rgb_to_hls(*(c / 255 for c in color))
            expected = colorsys.hls_to_rgb(hue, 1 - lightness, saturation)
            image = basemap.invert_lightness(Image.new("RGB", (1, 1), color))
            with self.subTest(color):
                for value, target in zip(image.getpixel((0, 0)), expected):
                    self.assertAlmostEqual(value, target * 255, delta=1)

    def test_twice_is_the_original(self):
        image = Image.new("RGBA", (1, 1), (120, 180, 240, 255))
        twice = basemap.invert_lightness(basemap.invert_lightness(image))
        self.assertEqual(twice.getpixel((0, 0)), (120, 180, 240, 255))


class MapWithBaseMapTestCase(unittest.TestCase):
    def setUp(self):
        basemap.get_basemap.cache_clear()
        self.addCleanup(basemap.get_basemap.cache_clear)
        patcher = patch("requests.get", side_effect=self.answer)
        self.get = patcher.start()
        self.addCleanup(patcher.stop)
        self.bkg_reachable = True

    def answer(self, url, **_):
        if urlparse(url).hostname == "maps.dwd.de":
            return response(weather_png())
        if self.bkg_reachable:
            return response(png(LAND))
        raise requests.ConnectionError

    def requests_to(self, hostname):
        urls = [call.args[0] for call in self.get.call_args_list]
        return [url for url in urls if urlparse(url).hostname == hostname]

    def get_map(self, background_types, **kwargs):
        return dwdmap.get_map(
            *SECTION,
            [dwdmap.WeatherMapType.NIEDERSCHLAGSRADAR],
            background_types,
            WIDTH,
            HEIGHT,
            **kwargs,
        )

    def loop(self):
        return dwdmap.ImageLoop(
            *SECTION,
            [dwdmap.WeatherMapType.NIEDERSCHLAGSRADAR],
            [dwdmap.WeatherBackgroundMapType.TOPPLUS_LIGHT],
            2,
            WIDTH,
            HEIGHT,
        )

    def test_without_basemap_nothing_changes(self):
        self.get_map([dwdmap.WeatherBackgroundMapType.KREISE])
        (url,) = (call.args[0] for call in self.get.call_args_list)
        query = parse_qs(urlparse(url).query)
        self.assertNotIn("transparent", query)
        self.assertEqual(
            query["layers"], ["dwd:Warngebiete_Kreise,dwd:Radar_rv_product_1x1km_ger"]
        )

    def test_basemap(self):
        image = self.get_map([dwdmap.WeatherBackgroundMapType.TOPPLUS_LIGHT])
        (url,) = self.requests_to("maps.dwd.de")
        query = parse_qs(urlparse(url).query)
        self.assertEqual(query["layers"], ["dwd:Radar_rv_product_1x1km_ger"])
        self.assertEqual(query["transparent"], ["true"])
        self.assertEqual(image.getpixel((0, 0)), RAIN)
        self.assertEqual(image.getpixel((WIDTH - 1, 0)), LAND)

    def test_dwd_layers_on_top_of_basemap(self):
        self.get_map(
            [
                dwdmap.WeatherBackgroundMapType.TOPPLUS_DARK,
                dwdmap.WeatherBackgroundMapType.LAENDER,
            ]
        )
        (url,) = self.requests_to("maps.dwd.de")
        self.assertEqual(
            parse_qs(urlparse(url).query)["layers"],
            ["dwd:Radar_rv_product_1x1km_ger,dwd:Laender"],
        )

    def test_basemap_is_shared_between_calls(self):
        self.get_map([dwdmap.WeatherBackgroundMapType.TOPPLUS_LIGHT])
        self.get_map([dwdmap.WeatherBackgroundMapType.TOPPLUS_LIGHT])
        self.assertEqual(len(self.requests_to("sgx.geodatenzentrum.de")), 1)
        self.assertEqual(len(self.requests_to("maps.dwd.de")), 2)

    def test_cache_dir(self):
        with tempfile.TemporaryDirectory() as directory:
            self.get_map(
                [dwdmap.WeatherBackgroundMapType.TOPPLUS_LIGHT],
                basemap_cache_dir=directory,
            )
            self.assertEqual(len(os.listdir(directory)), 1)

    def test_get_germany_and_location_pass_the_cache_dir(self):
        arguments = {
            "map_types": [dwdmap.WeatherMapType.NIEDERSCHLAGSRADAR],
            "background_types": [dwdmap.WeatherBackgroundMapType.TOPPLUS_LIGHT],
            "image_width": WIDTH,
            "image_height": HEIGHT,
        }
        with tempfile.TemporaryDirectory() as directory:
            dwdmap.get_germany(**arguments, basemap_cache_dir=directory)
            dwdmap.get_from_location(
                9, 49, 50, **arguments, basemap_cache_dir=directory
            )
            self.assertEqual(len(os.listdir(directory)), 2)

    def test_blend(self):
        # the blue of RAIN multiplied with LAND
        blended = (0, 0, LAND[2])
        types = {
            "map_types": [dwdmap.WeatherMapType.NIEDERSCHLAGSRADAR],
            "background_types": [dwdmap.WeatherBackgroundMapType.TOPPLUS_LIGHT],
            "image_width": WIDTH,
            "image_height": HEIGHT,
            "basemap_blend": True,
        }
        for name, image in {
            "get_map": dwdmap.get_map(*SECTION, **types),
            "get_germany": dwdmap.get_germany(**types),
            "get_from_location": dwdmap.get_from_location(9, 49, 50, **types),
            "ImageLoop": dwdmap.ImageLoop(*SECTION, steps=1, **types)[0],
        }.items():
            with self.subTest(name):
                self.assertEqual(image.getpixel((0, 0)), blended)

    def test_blank_background_without_basemap(self):
        self.bkg_reachable = False
        types = [dwdmap.WeatherBackgroundMapType.TOPPLUS_LIGHT]
        image = self.get_map(types)
        self.assertEqual(image.getpixel((0, 0)), RAIN)
        self.assertEqual(image.getpixel((WIDTH - 1, 0)), (255, 255, 255))
        image = self.get_map(types, dark_mode=True)
        self.assertEqual(image.getpixel((WIDTH - 1, 0)), (28, 28, 28))

    def test_marker_is_drawn_on_top(self):
        marker = dwdmap.Marker(49.5, 9.5, dwdmap.MarkerShape.SQUARE, 10, (255, 0, 0))
        image = self.get_map(
            [dwdmap.WeatherBackgroundMapType.TOPPLUS_LIGHT], markers=[marker]
        )
        self.assertEqual(image.getpixel((WIDTH // 2, HEIGHT // 2)), (255, 0, 0))

    @patch("simple_dwd_weatherforecast.dwdmap.get_time_last_5_min", return_value=SLOT)
    def test_loop(self, _):
        loop = self.loop()
        self.assertEqual(len(loop.get_images()), 2)
        self.assertEqual(len(self.requests_to("sgx.geodatenzentrum.de")), 1)
        for image in loop.get_images():
            self.assertEqual(image.getpixel((WIDTH - 1, 0)), LAND)

    @patch("simple_dwd_weatherforecast.dwdmap.get_time_last_5_min", return_value=SLOT)
    def test_loop_is_reloaded_when_the_basemap_is_back(self, _):
        self.bkg_reachable = False
        loop = self.loop()
        self.assertEqual(loop[0].getpixel((WIDTH - 1, 0)), (255, 255, 255))
        # still within the waiting time: no reload, DWD is not asked again
        self.bkg_reachable = True
        loop.update()
        self.assertEqual(len(self.requests_to("maps.dwd.de")), 2)
        loop._basemap._retry_after = None
        loop.update()
        self.assertEqual(loop[0].getpixel((WIDTH - 1, 0)), LAND)
        self.assertEqual(loop[1].getpixel((WIDTH - 1, 0)), LAND)
        # and only once
        self.assertEqual(len(self.requests_to("maps.dwd.de")), 4)
        loop.update()
        self.assertEqual(len(self.requests_to("maps.dwd.de")), 4)


if __name__ == "__main__":
    unittest.main()
