import os
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from unittest.mock import patch

try:
    import eccodes

    _ECCODES_AVAILABLE = True
except Exception:
    eccodes = None
    _ECCODES_AVAILABLE = False

from simple_dwd_weatherforecast import dwdforecast


def _make_grib2_data():
    """Create a minimal two-message GRIB2 byte string for testing.

    Covers Germany (55°N–47°N, 6°E–15°E) on a 10×10 grid.
    Base time: 2026-04-01T00:00Z.
    Message 0: step +6 h  -> validityTime 2026-04-01T06:00Z, values 16.0 °C.
    Message 1: step +12 h -> validityTime 2026-04-01T12:00Z, values 22.0 °C.
    """
    messages = []
    for step, value in [(6, 16.0), (12, 22.0)]:
        msg_id = eccodes.codes_grib_new_from_samples("regular_ll_pl_grib2")
        try:
            eccodes.codes_set(msg_id, "Ni", 10)
            eccodes.codes_set(msg_id, "Nj", 10)
            eccodes.codes_set(msg_id, "latitudeOfFirstGridPointInDegrees", 55.0)
            eccodes.codes_set(msg_id, "longitudeOfFirstGridPointInDegrees", 6.0)
            eccodes.codes_set(msg_id, "latitudeOfLastGridPointInDegrees", 47.0)
            eccodes.codes_set(msg_id, "longitudeOfLastGridPointInDegrees", 15.0)
            eccodes.codes_set(msg_id, "iDirectionIncrementInDegrees", 1.0)
            eccodes.codes_set(msg_id, "jDirectionIncrementInDegrees", 0.889)
            eccodes.codes_set(msg_id, "year", 2026)
            eccodes.codes_set(msg_id, "month", 4)
            eccodes.codes_set(msg_id, "day", 1)
            eccodes.codes_set(msg_id, "hour", 0)
            eccodes.codes_set(msg_id, "minute", 0)
            eccodes.codes_set(msg_id, "second", 0)
            eccodes.codes_set(msg_id, "stepRange", str(step))
            eccodes.codes_set_values(msg_id, [value] * 100)

            tmp_fd, tmp_path = tempfile.mkstemp(suffix=".grb2")
            try:
                with os.fdopen(tmp_fd, "wb") as fout:
                    eccodes.codes_write(msg_id, fout)
                with open(tmp_path, "rb") as fin:
                    messages.append(fin.read())
            finally:
                if os.path.exists(tmp_path):
                    os.unlink(tmp_path)
        finally:
            eccodes.codes_release(msg_id)

    return b"".join(messages)


_GRIB2_DATA = _make_grib2_data() if _ECCODES_AVAILABLE else b""


@unittest.skipUnless(_ECCODES_AVAILABLE, "eccodes backend is not available")
class ApparentTemperatureTestCase(unittest.TestCase):
    def setUp(self):
        self.dwd_weather = dwdforecast.Weather("10438")  # Kassel

    # ------------------------------------------------------------------
    # _parse_apparent_temperature_grib
    # ------------------------------------------------------------------
    def test_parse_grib_returns_dict(self):
        result = self.dwd_weather._parse_apparent_temperature_grib(iter([_GRIB2_DATA]))
        self.assertIsInstance(result, dict)

    def test_parse_grib_two_timesteps(self):
        result = self.dwd_weather._parse_apparent_temperature_grib(iter([_GRIB2_DATA]))
        self.assertEqual(len(result), 2)

    def test_parse_grib_correct_timestamps(self):
        result = self.dwd_weather._parse_apparent_temperature_grib(iter([_GRIB2_DATA]))
        self.assertIn("2026-04-01T06:00:00.000Z", result)
        self.assertIn("2026-04-01T12:00:00.000Z", result)

    def test_parse_grib_values_are_celsius(self):
        result = self.dwd_weather._parse_apparent_temperature_grib(iter([_GRIB2_DATA]))
        # Values should be reasonable Celsius temperatures (not Kelvin)
        for v in result.values():
            self.assertLess(v, 100.0)
            self.assertGreater(v, -100.0)

    # ------------------------------------------------------------------
    # get_apparent_temperature
    # ------------------------------------------------------------------
    def test_get_apparent_temperature_known_value(self):
        now_key = self.dwd_weather.strip_to_hour_str(datetime.now(timezone.utc))
        self.dwd_weather.apparent_temperature_data = {now_key: 16.0}
        value = self.dwd_weather.get_apparent_temperature(shouldUpdate=False)
        self.assertIsNotNone(value)
        self.assertIsInstance(value, float)

    def test_get_apparent_temperature_not_in_range(self):
        self.dwd_weather.apparent_temperature_data = {
            "2026-04-01T06:00:00.000Z": 16.0,
            "2026-04-01T12:00:00.000Z": 22.0,
        }
        value = self.dwd_weather.get_apparent_temperature(shouldUpdate=False)
        self.assertIsNone(value)

    def test_get_apparent_temperature_no_data_no_update(self):
        self.dwd_weather.apparent_temperature_data = None
        value = self.dwd_weather.get_apparent_temperature(shouldUpdate=False)
        self.assertIsNone(value)

    def test_get_apparent_temperature_calls_update(self):
        with patch.object(self.dwd_weather, "download_apparent_temperature") as mock_dl:
            self.dwd_weather.apparent_temperature_data = None
            self.dwd_weather.get_apparent_temperature(shouldUpdate=True)
            mock_dl.assert_called_once()

    # ------------------------------------------------------------------
    # get_apparent_temperature_forecast
    # ------------------------------------------------------------------
    def test_get_apparent_temperature_forecast_returns_data(self):
        now_hour = datetime.now(timezone.utc).replace(minute=0, second=0, microsecond=0)
        now_key = self.dwd_weather.strip_to_hour_str(now_hour)
        next_key = self.dwd_weather.strip_to_hour_str(now_hour + timedelta(hours=1))
        self.dwd_weather.apparent_temperature_data = {
            self.dwd_weather.strip_to_hour_str(now_hour - timedelta(hours=1)): 9.0,
            now_key: 10.0,
            next_key: 12.0,
        }
        result = self.dwd_weather.get_apparent_temperature_forecast(shouldUpdate=False)
        self.assertEqual(
            result,
            {
                now_key: 10.0,
                next_key: 12.0,
            },
        )

    def test_get_apparent_temperature_forecast_no_data_no_update(self):
        self.dwd_weather.apparent_temperature_data = None
        result = self.dwd_weather.get_apparent_temperature_forecast(shouldUpdate=False)
        self.assertIsNone(result)

    # ------------------------------------------------------------------
    # update() with_apparent_temperature flag
    # ------------------------------------------------------------------
    @patch(
        "simple_dwd_weatherforecast.dwdforecast.Weather.download_apparent_temperature",
        return_value=None,
    )
    @patch(
        "simple_dwd_weatherforecast.dwdforecast.Weather.download_latest_kml",
        return_value=None,
    )
    def test_update_with_apparent_temperature(self, _kml, mock_dl):
        self.dwd_weather.update(
            with_forecast=False,
            with_uv=False,
            with_apparent_temperature=True,
        )
        mock_dl.assert_called_once()

    @patch(
        "simple_dwd_weatherforecast.dwdforecast.Weather.download_apparent_temperature",
        return_value=None,
    )
    @patch(
        "simple_dwd_weatherforecast.dwdforecast.Weather.download_latest_kml",
        return_value=None,
    )
    def test_update_without_apparent_temperature(self, _kml, mock_dl):
        self.dwd_weather.update(
            with_forecast=False,
            with_uv=False,
            with_apparent_temperature=False,
        )
        mock_dl.assert_not_called()
