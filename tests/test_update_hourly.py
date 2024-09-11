import unittest
from unittest.mock import patch
from simple_dwd_weatherforecast import dwdforecast
from dummy_data import parsed_data
from datetime import datetime, timezone
import time


class WeatherUpdate(unittest.TestCase):
    def setUp(self):
        self.dwd_weather = dwdforecast.Weather("H889")
        self.dwd_weather.forecast_data = parsed_data  # type: ignore

    def test_download(self):
        self.dwd_weather.update(force_hourly=True)
        self.assertIsNotNone(self.dwd_weather.forecast_data)
        self.assertEqual(self.dwd_weather.station_id, "H889")
        self.assertEqual(self.dwd_weather.issue_time.date(), datetime.now().date())  # type: ignore

    @patch(
        "simple_dwd_weatherforecast.dwdforecast.Weather.download_latest_kml",
        return_value=None,
    )
    def test_issue_time_none(self, mock_function):
        self.dwd_weather.update()
        mock_function.assert_called()

    @patch(
        "simple_dwd_weatherforecast.dwdforecast.Weather.download_latest_kml",
        return_value=None,
    )
    def test_issue_time_old(self, mock_function):
        self.dwd_weather.issue_time = datetime(
            *(time.strptime("2020-11-06T03:00:00.000Z", "%Y-%m-%dT%H:%M:%S.%fZ")[0:6]),
            0,
            timezone.utc
        )
        self.dwd_weather.update()
        mock_function.assert_called()

    @patch(
        "simple_dwd_weatherforecast.dwdforecast.Weather.download_latest_kml",
        return_value=None,
    )
    @patch(
        "simple_dwd_weatherforecast.dwdforecast.Weather.parse_kml", return_value=None
    )
    def test_issue_time_actual(self, mock_function, _):
        self.dwd_weather.issue_time = datetime.now(timezone.utc)
        self.dwd_weather.update()
        mock_function.assert_not_called()
