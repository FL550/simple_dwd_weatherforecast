import unittest
from unittest.mock import patch
from simple_dwd_weatherforecast import dwdmap
from datetime import datetime, timedelta, timezone


class MapTestCase(unittest.TestCase):
    def test_prevent_too_large_height(self):
        with self.assertRaises(ValueError):
            dwdmap.get_map(
                4.4,
                46.4,
                16.1,
                55.6,
                dwdmap.WeatherMapType.NIEDERSCHLAGSRADAR,
                dwdmap.WeatherBackgroundMapType.BUNDESLAENDER,
                1300,
                700,
            )

    def test_prevent_too_large_width(self):
        with self.assertRaises(ValueError):
            dwdmap.get_map(
                4.4,
                46.4,
                16.1,
                55.6,
                dwdmap.WeatherMapType.NIEDERSCHLAGSRADAR,
                dwdmap.WeatherBackgroundMapType.BUNDESLAENDER,
                300,
                1700,
            )

    def test_prevent_too_large(self):
        with self.assertRaises(ValueError):
            dwdmap.get_map(
                4.4,
                46.4,
                16.1,
                55.6,
                dwdmap.WeatherMapType.NIEDERSCHLAGSRADAR,
                dwdmap.WeatherBackgroundMapType.BUNDESLAENDER,
                1300,
                1700,
            )


class ImageLoopTestCase(unittest.TestCase):
    @patch("simple_dwd_weatherforecast.dwdmap.ImageLoop._get_image", return_value=None)
    def test_init(self, mock_function):
        maploop = dwdmap.ImageLoop(
            0.1,
            0.2,
            0.3,
            0.4,
            dwdmap.WeatherMapType.NIEDERSCHLAGSRADAR,
            dwdmap.WeatherBackgroundMapType.BUNDESLAENDER,
            1,
        )
        self.assertEqual(
            maploop._minx,
            0.1,
        )
        self.assertEqual(
            maploop._miny,
            0.2,
        )
        self.assertEqual(
            maploop._maxx,
            0.3,
        )
        self.assertEqual(
            maploop._maxy,
            0.4,
        )
        self.assertEqual(
            maploop._map_type,
            dwdmap.WeatherMapType.NIEDERSCHLAGSRADAR,
        )
        self.assertEqual(
            maploop._background_type,
            dwdmap.WeatherBackgroundMapType.BUNDESLAENDER,
        )
        mock_function.assert_called_once()

    @patch("simple_dwd_weatherforecast.dwdmap.ImageLoop._get_image", return_value=None)
    def test_steps1(self, mock_function):
        _ = dwdmap.ImageLoop(
            0.1,
            0.2,
            0.3,
            0.4,
            dwdmap.WeatherMapType.NIEDERSCHLAGSRADAR,
            dwdmap.WeatherBackgroundMapType.BUNDESLAENDER,
            5,
        )
        self.assertEqual(mock_function.call_count, 5)

    @patch("simple_dwd_weatherforecast.dwdmap.ImageLoop._get_image", return_value=None)
    def test_steps2(self, mock_function):
        _ = dwdmap.ImageLoop(
            0.1,
            0.2,
            0.3,
            0.4,
            dwdmap.WeatherMapType.NIEDERSCHLAGSRADAR,
            dwdmap.WeatherBackgroundMapType.BUNDESLAENDER,
            10,
        )
        self.assertEqual(mock_function.call_count, 10)

    @patch("simple_dwd_weatherforecast.dwdmap.ImageLoop._get_image", return_value=None)
    def test_update_full(self, mock_function):
        maploop = dwdmap.ImageLoop(
            0.1,
            0.2,
            0.3,
            0.4,
            dwdmap.WeatherMapType.NIEDERSCHLAGSRADAR,
            dwdmap.WeatherBackgroundMapType.BUNDESLAENDER,
            5,
        )
        maploop._last_update = datetime(year=2024, month=9, day=4, hour=5, minute=50)
        self.assertEqual(mock_function.call_count, 5)

    @patch("simple_dwd_weatherforecast.dwdmap.ImageLoop._get_image", return_value=None)
    def test_update_part(self, mock_function):
        maploop = dwdmap.ImageLoop(
            0.1,
            0.2,
            0.3,
            0.4,
            dwdmap.WeatherMapType.NIEDERSCHLAGSRADAR,
            dwdmap.WeatherBackgroundMapType.BUNDESLAENDER,
            5,
        )
        now = dwdmap.get_time_last_5_min(datetime.now(timezone.utc))
        maploop._last_update = now - timedelta(minutes=15)
        mock_function.reset_mock()
        maploop.update()
        self.assertEqual(mock_function.call_count, 3)


class GeneralTestCase(unittest.TestCase):
    def test_get_time_last_5_min_strip(self):
        time = datetime(year=2024, month=9, day=4, hour=9, minute=50, second=52)
        self.assertEqual(
            dwdmap.get_time_last_5_min(time),
            datetime(year=2024, month=9, day=4, hour=9, minute=50),
        )

    def test_get_time_last_5_min_exact(self):
        time = datetime(year=2024, month=9, day=4, hour=9, minute=50, second=00)
        self.assertEqual(
            dwdmap.get_time_last_5_min(time),
            datetime(year=2024, month=9, day=4, hour=9, minute=50),
        )

    def test_get_time_last_5_min_between1(self):
        time = datetime(year=2024, month=9, day=4, hour=9, minute=52, second=00)
        self.assertEqual(
            dwdmap.get_time_last_5_min(time),
            datetime(year=2024, month=9, day=4, hour=9, minute=50),
        )

    def test_get_time_last_5_min_between2(self):
        time = datetime(year=2024, month=9, day=4, hour=9, minute=3, second=00)
        self.assertEqual(
            dwdmap.get_time_last_5_min(time),
            datetime(year=2024, month=9, day=4, hour=9, minute=0),
        )
