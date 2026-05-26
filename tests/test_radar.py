import struct
import tarfile
import unittest
from datetime import UTC, datetime, timedelta
from io import BytesIO
from unittest.mock import MagicMock, patch

from simple_dwd_weatherforecast import dwdforecast
from simple_dwd_weatherforecast.dwdradar import (
    DWDRadar,
    NotInAreaError,
    RadarNotAvailableError,
    _DIRECTION_DEGREES,
    _DIRECTION_SCAN_RADIUS,
    _DIRECTIONS,
    _linear_interp,
)


def _make_radar_frame(x_cart: int, y_cart: int, value_raw: int) -> bytes:
    """Build a radar frame with a compact 2x2 wet patch around a grid cell."""
    return _make_radar_frame_points(
        [
            (x_cart, y_cart),
            (x_cart + 1, y_cart),
            (x_cart, y_cart + 1),
            (x_cart + 1, y_cart + 1),
        ],
        value_raw,
    )


def _make_radar_frame_points(points: list[tuple[int, int]], value_raw: int) -> bytes:
    """Build a binary radar frame with rain values at specific coordinates."""
    xsize = 1100
    ysize = 1200
    num_values = xsize * ysize
    data = bytearray(num_values * 2)
    for x_cart, y_cart in points:
        if 0 <= x_cart < xsize and 0 <= y_cart < ysize:
            idx = (y_cart * xsize + x_cart) * 2
            struct.pack_into("<H", data, idx, value_raw)
    return bytes(data)


def _make_radar_frame_direction(
    x_cart: int, y_cart: int, dx: int, dy: int, radius: int, value_raw: int
) -> bytes:
    """Build a radar frame with rain pixels along (dx, dy) from the origin."""
    xsize = 1100
    ysize = 1200
    num_values = xsize * ysize
    data = bytearray(num_values * 2)
    for step in range(1, radius + 1):
        nx = x_cart + dx * step
        ny = y_cart + dy * step
        if 0 <= nx < xsize and 0 <= ny < ysize:
            struct.pack_into("<H", data, (ny * xsize + nx) * 2, value_raw)
    return bytes(data)


def _make_tar_bz2(frames: dict) -> bytes:
    """Build an in-memory tar.bz2 archive with radar frames."""
    buf = BytesIO()
    with tarfile.open(fileobj=buf, mode="w:bz2") as tar:
        for name, content in frames.items():
            full = b"HEADER\x03" + content
            info = tarfile.TarInfo(name=name)
            info.size = len(full)
            tar.addfile(info, BytesIO(full))
    return buf.getvalue()


class TestLinearInterp(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(_linear_interp(5.0, [], []), 0.0)

    def test_below_range(self):
        self.assertEqual(_linear_interp(0.0, [1.0, 2.0], [10.0, 20.0]), 10.0)

    def test_above_range(self):
        self.assertEqual(_linear_interp(3.0, [1.0, 2.0], [10.0, 20.0]), 20.0)

    def test_exact_point(self):
        self.assertAlmostEqual(_linear_interp(1.5, [1.0, 2.0], [10.0, 20.0]), 15.0)

    def test_midpoint(self):
        self.assertAlmostEqual(_linear_interp(1.5, [1.0, 2.0], [0.0, 1.0]), 0.5)


class TestDWDRadarDecodeValue(unittest.TestCase):
    def setUp(self):
        self.radar = DWDRadar()

    def test_no_data_flag(self):
        # Bit 13 set => no data
        self.assertEqual(self.radar._decode_value(0b0010000000000000), 0.0)

    def test_zero(self):
        self.assertEqual(self.radar._decode_value(0), 0.0)

    def test_typical_value(self):
        # raw=100 => 100/100*12 = 12.0 mm/h
        self.assertAlmostEqual(self.radar._decode_value(100), 12.0)

    def test_small_value(self):
        # raw=10 => 10/100*12 = 1.2 mm/h
        self.assertAlmostEqual(self.radar._decode_value(10), 1.2)


class TestDWDRadarGridIndex(unittest.TestCase):
    def setUp(self):
        # Provide minimal radar data so _radars is not None
        self.radar = DWDRadar()
        dummy_frame = bytes(1100 * 1200 * 2)
        self.radar._radars = {datetime(2024, 1, 1, tzinfo=UTC): dummy_frame}

    def test_central_germany(self):
        # Berlin approx lat=52.52, lon=13.41 should be within bounds
        x, y = self.radar._get_grid_index(52.52, 13.41)
        self.assertTrue(0 <= x < 1100)
        self.assertTrue(0 <= y < 1200)

    def test_out_of_area(self):
        # Coordinates far outside Germany (e.g. New York)
        with self.assertRaises(NotInAreaError):
            self.radar._get_grid_index(40.71, -74.01)

    def test_no_data_raises(self):
        radar = DWDRadar()
        with self.assertRaises(RadarNotAvailableError):
            radar._get_grid_index(52.52, 13.41)


class TestDWDRadarGetPrecipitationValues(unittest.TestCase):
    def setUp(self):
        self.radar = DWDRadar()
        # Find grid index for Berlin
        tmp_radar = DWDRadar()
        tmp_radar._radars = {datetime(2024, 1, 1, tzinfo=UTC): bytes(1100 * 1200 * 2)}
        self.berlin_x, self.berlin_y = tmp_radar._get_grid_index(52.52, 13.41)

        t1 = datetime(2024, 4, 1, 12, 0, tzinfo=UTC)
        t2 = datetime(2024, 4, 1, 12, 5, tzinfo=UTC)
        # raw=100 => 12.0 mm/h for t1; 0 for t2
        frame1 = _make_radar_frame(self.berlin_x, self.berlin_y, 100)
        frame2 = _make_radar_frame(self.berlin_x, self.berlin_y, 0)
        self.radar._radars = {t1: frame1, t2: frame2}
        self.t1 = t1
        self.t2 = t2

    def test_returns_sorted_dict(self):
        values = self.radar.get_precipitation_values(52.52, 13.41)
        keys = list(values.keys())
        self.assertEqual(keys, sorted(keys))

    def test_values_correct(self):
        values = self.radar.get_precipitation_values(52.52, 13.41)
        self.assertAlmostEqual(values[self.t1], 12.0)
        self.assertAlmostEqual(values[self.t2], 0.0)

    def test_no_data_raises(self):
        radar = DWDRadar()
        with self.assertRaises(RadarNotAvailableError):
            radar.get_precipitation_values(52.52, 13.41)

    def test_out_of_area_raises(self):
        with self.assertRaises(NotInAreaError):
            self.radar.get_precipitation_values(40.71, -74.01)

    def test_single_pixel_noise_is_filtered(self):
        radar = DWDRadar()
        t1 = datetime(2024, 4, 1, 12, 0, tzinfo=UTC)
        radar._radars = {
            t1: _make_radar_frame_points([(self.berlin_x, self.berlin_y)], 100)
        }
        values = radar.get_precipitation_values(52.52, 13.41)
        self.assertAlmostEqual(values[t1], 0.0)


class TestDWDRadarGetCurrentPrecipitation(unittest.TestCase):
    def setUp(self):
        self.radar = DWDRadar()
        tmp_radar = DWDRadar()
        tmp_radar._radars = {datetime(2024, 1, 1, tzinfo=UTC): bytes(1100 * 1200 * 2)}
        berlin_x, berlin_y = tmp_radar._get_grid_index(52.52, 13.41)

        t1 = datetime(2024, 4, 1, 12, 0, tzinfo=UTC)
        t2 = datetime(2024, 4, 1, 12, 5, tzinfo=UTC)
        frame1 = _make_radar_frame(berlin_x, berlin_y, 0)
        frame2 = _make_radar_frame(berlin_x, berlin_y, 100)  # 12.0 mm/h
        self.radar._radars = {t1: frame1, t2: frame2}
        self.t1 = t1
        self.t2 = t2

    def test_interpolation_midpoint(self):
        mid = datetime(2024, 4, 1, 12, 2, 30, tzinfo=UTC)
        result = self.radar.get_current_precipitation(52.52, 13.41, mid)
        self.assertAlmostEqual(result, 6.0, places=1)

    def test_at_exact_start(self):
        result = self.radar.get_current_precipitation(52.52, 13.41, self.t1)
        self.assertAlmostEqual(result, 0.0)

    def test_at_exact_end(self):
        result = self.radar.get_current_precipitation(52.52, 13.41, self.t2)
        self.assertAlmostEqual(result, 12.0)


class TestDWDRadarGetNextPrecipitation(unittest.TestCase):
    def _setup_radar(self, values_sequence):
        """Create a radar with given precipitation values at 5-min intervals."""
        radar = DWDRadar()
        tmp = DWDRadar()
        tmp._radars = {datetime(2024, 1, 1, tzinfo=UTC): bytes(1100 * 1200 * 2)}
        bx, by = tmp._get_grid_index(52.52, 13.41)
        base_time = datetime(2024, 4, 1, 12, 0, tzinfo=UTC)
        radars = {}
        for i, raw_val in enumerate(values_sequence):
            t = base_time + timedelta(minutes=5 * i)
            radars[t] = _make_radar_frame(bx, by, raw_val)
        radar._radars = radars
        return radar

    def test_no_rain(self):
        radar = self._setup_radar([0, 0, 0, 0])
        result = radar.get_next_precipitation(52.52, 13.41)
        self.assertIsNone(result["start"])
        self.assertIsNone(result["end"])
        self.assertIsNone(result["length"])
        self.assertEqual(result["max"], 0.0)
        self.assertEqual(result["sum"], 0.0)

    def test_rain_throughout(self):
        # raw=100 => 12.0 mm/h; rain from start to end of data
        radar = self._setup_radar([100, 100, 100, 100])
        result = radar.get_next_precipitation(52.52, 13.41)
        self.assertIsNotNone(result["start"])
        self.assertIsNone(result["end"])
        self.assertIsNone(result["length"])
        self.assertAlmostEqual(result["max"], 12.0)

    def test_rain_then_stops(self):
        # Rain for first 2 steps (t0, t1), then clear
        radar = self._setup_radar([100, 100, 0, 0])
        result = radar.get_next_precipitation(52.52, 13.41)
        base_time = datetime(2024, 4, 1, 12, 0, tzinfo=UTC)
        self.assertEqual(result["start"], base_time)
        self.assertEqual(result["end"], base_time + timedelta(minutes=10))
        self.assertEqual(result["length"], timedelta(minutes=10))
        self.assertAlmostEqual(result["max"], 12.0)

    def test_rain_starts_later(self):
        # No rain first step, then rain
        radar = self._setup_radar([0, 0, 100, 0, 0])
        result = radar.get_next_precipitation(52.52, 13.41)
        base_time = datetime(2024, 4, 1, 12, 0, tzinfo=UTC)
        self.assertEqual(result["start"], base_time + timedelta(minutes=10))


class TestDWDRadarUpdate(unittest.TestCase):
    def test_update_populates_radars(self):
        """Test that update() correctly parses a tar.bz2 archive."""
        # Name format: last 14 chars before last 3 = timestamp, last 3 = delta
        # e.g. "DE1200_RV_2404011200_000"
        frames = {
            "DE1200_RV_2404011200_000": bytes(1100 * 1200 * 2),
            "DE1200_RV_2404011200_005": bytes(1100 * 1200 * 2),
        }
        tar_data = _make_tar_bz2(frames)
        mock_response = MagicMock()
        mock_response.content = tar_data
        mock_response.raise_for_status = MagicMock()

        with patch("simple_dwd_weatherforecast.dwdradar.requests.get") as mock_get:
            mock_get.return_value = mock_response
            radar = DWDRadar()
            radar.update()

        self.assertIsNotNone(radar._radars)
        self.assertEqual(len(radar._radars), 2)
        # Check timestamps
        expected_t0 = datetime(2024, 4, 1, 12, 0, tzinfo=UTC)
        expected_t1 = datetime(2024, 4, 1, 12, 5, tzinfo=UTC)
        self.assertIn(expected_t0, radar._radars)
        self.assertIn(expected_t1, radar._radars)

    def test_update_handles_network_error(self):
        """Test that update() handles network errors gracefully."""
        with patch(
            "simple_dwd_weatherforecast.dwdradar.requests.get",
            side_effect=ConnectionError("Network error"),
        ):
            radar = DWDRadar()
            radar.update()  # should not raise
        self.assertIsNone(radar._radars)

    def test_update_uses_etag_and_handles_304(self):
        """Test that update() sends If-None-Match and keeps cached data on 304."""
        frames = {
            "DE1200_RV_2404011200_000": bytes(1100 * 1200 * 2),
        }
        tar_data = _make_tar_bz2(frames)

        first_response = MagicMock()
        first_response.status_code = 200
        first_response.content = tar_data
        first_response.raise_for_status = MagicMock()
        first_response.headers = {"ETag": '"abc123"'}

        second_response = MagicMock()
        second_response.status_code = 304
        second_response.raise_for_status = MagicMock()

        with patch("simple_dwd_weatherforecast.dwdradar.requests.get") as mock_get:
            mock_get.side_effect = [first_response, second_response]
            radar = DWDRadar()
            radar.update()
            original_radars = radar._radars
            radar.update()

        self.assertEqual(mock_get.call_count, 2)
        self.assertEqual(mock_get.call_args_list[0].kwargs.get("headers"), None)
        self.assertEqual(
            mock_get.call_args_list[1].kwargs.get("headers"),
            {"If-None-Match": '"abc123"'},
        )
        self.assertEqual(radar._etag, '"abc123"')
        self.assertIs(radar._radars, original_radars)


class TestWeatherRadarMethods(unittest.TestCase):
    def setUp(self):
        self.dwd_weather = dwdforecast.Weather("L821")
        # Provide mock radar data
        tmp = DWDRadar()
        tmp._radars = {datetime(2024, 1, 1, tzinfo=UTC): bytes(1100 * 1200 * 2)}
        bx, by = tmp._get_grid_index(
            float(self.dwd_weather.station["lat"]),
            float(self.dwd_weather.station["lon"]),
        )
        t1 = datetime(2024, 4, 1, 12, 0, tzinfo=UTC)
        t2 = datetime(2024, 4, 1, 12, 5, tzinfo=UTC)
        frame1 = _make_radar_frame(bx, by, 50)  # some rain
        frame2 = _make_radar_frame(bx, by, 0)  # no rain
        self.dwd_weather._radar._radars = {t1: frame1, t2: frame2}
        self.t1 = t1
        self.t2 = t2

    def test_get_radar_precipitation_forecast_no_update(self):
        result = self.dwd_weather.get_radar_precipitation_forecast(shouldUpdate=False)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)
        self.assertIn(self.t1, result)
        self.assertIn(self.t2, result)

    def test_get_radar_precipitation_forecast_uses_station_coords(self):
        # Without explicit lat/lon, uses station coords
        result = self.dwd_weather.get_radar_precipitation_forecast(shouldUpdate=False)
        self.assertIsNotNone(result)

    def test_get_radar_precipitation_forecast_explicit_coords(self):
        # With explicit coords (still in Germany)
        result = self.dwd_weather.get_radar_precipitation_forecast(
            lat=52.52, lon=13.41, shouldUpdate=False
        )
        self.assertIsNotNone(result)

    def test_get_radar_precipitation_forecast_out_of_area(self):
        result = self.dwd_weather.get_radar_precipitation_forecast(
            lat=40.71, lon=-74.01, shouldUpdate=False
        )
        self.assertIsNone(result)

    def test_get_radar_next_precipitation_no_update(self):
        result = self.dwd_weather.get_radar_next_precipitation(shouldUpdate=False)
        self.assertIsNotNone(result)
        self.assertIn("start", result)
        self.assertIn("end", result)
        self.assertIn("length", result)
        self.assertIn("max", result)
        self.assertIn("sum", result)

    def test_get_radar_next_precipitation_out_of_area(self):
        result = self.dwd_weather.get_radar_next_precipitation(
            lat=40.71, lon=-74.01, shouldUpdate=False
        )
        self.assertIsNone(result)

    @patch("simple_dwd_weatherforecast.dwdforecast.DWDRadar.update")
    def test_get_radar_precipitation_forecast_calls_update(self, mock_update):
        mock_update.return_value = None
        self.dwd_weather.get_radar_precipitation_forecast(shouldUpdate=True)
        mock_update.assert_called_once()

    @patch("simple_dwd_weatherforecast.dwdforecast.DWDRadar.update")
    def test_get_radar_next_precipitation_calls_update(self, mock_update):
        mock_update.return_value = None
        self.dwd_weather.get_radar_next_precipitation(shouldUpdate=True)
        mock_update.assert_called_once()


class TestDWDRadarDirection(unittest.TestCase):
    """Tests for the rain-direction helpers in DWDRadar."""

    def _make_radar(self, pre_frames, rain_frame, berlin_x, berlin_y):
        """Return a DWDRadar with look-back frames followed by rain at location."""
        radar = DWDRadar()
        base = datetime(2024, 4, 1, 12, 0, tzinfo=UTC)
        radars = {}
        for i, frame in enumerate(pre_frames):
            radars[base + timedelta(minutes=5 * i)] = frame
        rain_t = base + timedelta(minutes=5 * len(pre_frames))
        radars[rain_t] = rain_frame
        radar._radars = radars
        return radar, rain_t

    def setUp(self):
        tmp = DWDRadar()
        tmp._radars = {datetime(2024, 1, 1, tzinfo=UTC): bytes(1100 * 1200 * 2)}
        self.bx, self.by = tmp._get_grid_index(52.52, 13.41)

    def test_no_lookback_returns_none(self):
        """When rain starts at the first frame there is no look-back data."""
        rain_frame = _make_radar_frame(self.bx, self.by, 100)
        radar = DWDRadar()
        base = datetime(2024, 4, 1, 12, 0, tzinfo=UTC)
        radar._radars = {base: rain_frame}
        deg, label = radar._determine_rain_direction(self.bx, self.by, base)
        self.assertIsNone(deg)
        self.assertIsNone(label)

    def test_direction_north(self):
        """Rain pixels north of the location → direction should be N."""
        # North: dx=0, dy=-1
        dx, dy = 0, -1
        pre_frame = _make_radar_frame_direction(
            self.bx, self.by, dx, dy, _DIRECTION_SCAN_RADIUS, 100
        )
        rain_frame = _make_radar_frame(self.bx, self.by, 100)
        radar, rain_t = self._make_radar([pre_frame], rain_frame, self.bx, self.by)
        deg, label = radar._determine_rain_direction(self.bx, self.by, rain_t)
        self.assertEqual(label, "N")
        self.assertAlmostEqual(deg, _DIRECTION_DEGREES["N"])

    def test_direction_southwest(self):
        """Rain pixels southwest → direction should be SW."""
        dx, dy = -1, 1
        pre_frame = _make_radar_frame_direction(
            self.bx, self.by, dx, dy, _DIRECTION_SCAN_RADIUS, 100
        )
        rain_frame = _make_radar_frame(self.bx, self.by, 100)
        radar, rain_t = self._make_radar([pre_frame], rain_frame, self.bx, self.by)
        deg, label = radar._determine_rain_direction(self.bx, self.by, rain_t)
        self.assertEqual(label, "SW")
        self.assertAlmostEqual(deg, _DIRECTION_DEGREES["SW"])

    def test_get_next_precipitation_includes_direction_keys(self):
        """get_next_precipitation result must always contain direction keys."""
        # Build a radar with no rain at all
        radar = DWDRadar()
        base = datetime(2024, 4, 1, 12, 0, tzinfo=UTC)
        radar._radars = {
            base: _make_radar_frame(self.bx, self.by, 0),
            base + timedelta(minutes=5): _make_radar_frame(self.bx, self.by, 0),
        }
        result = radar.get_next_precipitation(52.52, 13.41)
        self.assertIn("direction_deg", result)
        self.assertIn("direction", result)
        self.assertIsNone(result["direction_deg"])
        self.assertIsNone(result["direction"])

    def test_get_next_precipitation_direction_when_rain_from_east(self):
        """Direction is detected correctly in the full get_next_precipitation flow."""
        dx, dy = 1, 0  # East
        pre_frame = _make_radar_frame_direction(
            self.bx, self.by, dx, dy, _DIRECTION_SCAN_RADIUS, 100
        )
        rain_frame = _make_radar_frame(self.bx, self.by, 100)
        radar, _ = self._make_radar([pre_frame], rain_frame, self.bx, self.by)
        result = radar.get_next_precipitation(52.52, 13.41)
        self.assertEqual(result["direction"], "E")
        self.assertAlmostEqual(result["direction_deg"], 90.0)

    def test_scan_directions_all_zero(self):
        """_scan_directions returns 0 for all directions on an empty frame."""
        empty_frame = bytes(1100 * 1200 * 2)
        radar = DWDRadar()
        radar._radars = {datetime(2024, 1, 1, tzinfo=UTC): empty_frame}
        scan = radar._scan_directions(self.bx, self.by, empty_frame, 5)
        for label, *_ in _DIRECTIONS:
            self.assertEqual(scan[label], 0.0)

    def test_get_grid_value_out_of_bounds(self):
        """_get_grid_value returns 0 for coordinates outside the grid."""
        radar = DWDRadar()
        frame = bytes(1100 * 1200 * 2)
        self.assertEqual(radar._get_grid_value(-1, 0, frame), 0.0)
        self.assertEqual(radar._get_grid_value(0, -1, frame), 0.0)
        self.assertEqual(radar._get_grid_value(1100, 0, frame), 0.0)
        self.assertEqual(radar._get_grid_value(0, 1200, frame), 0.0)

    def test_get_radar_next_precipitation_includes_direction_keys(self):
        """dwdforecast.get_radar_next_precipitation exposes direction keys."""
        dwd_weather = dwdforecast.Weather("L821")
        tmp = DWDRadar()
        tmp._radars = {datetime(2024, 1, 1, tzinfo=UTC): bytes(1100 * 1200 * 2)}
        bx, by = tmp._get_grid_index(
            float(dwd_weather.station["lat"]),
            float(dwd_weather.station["lon"]),
        )
        base = datetime(2024, 4, 1, 12, 0, tzinfo=UTC)
        dwd_weather._radar._radars = {
            base: _make_radar_frame(bx, by, 0),
        }
        result = dwd_weather.get_radar_next_precipitation(shouldUpdate=False)
        self.assertIn("direction_deg", result)
        self.assertIn("direction", result)
