import unittest
from unittest.mock import patch
from datetime import datetime, timedelta
from simple_dwd_weatherforecast import dwdforecast
from dummy_data import parsed_data


class Weather_get_timeframe_condition(unittest.TestCase):
    def setUp(self):
        self.dwd_weather = dwdforecast.Weather("H889")
        self.dwd_weather.forecast_data = parsed_data  # type: ignore

    @patch("simple_dwd_weatherforecast.dwdforecast.Weather.update", return_value=None)
    def test_shouldupdate(self, mock_update):
        test_time = datetime(2020, 11, 7, 3, 30)
        self.dwd_weather.get_timeframe_condition(test_time, 3, True)
        mock_update.assert_called()

    @patch("simple_dwd_weatherforecast.dwdforecast.Weather.update", return_value=None)
    def test_shouldupdate_not(self, mock_update):
        test_time = datetime(2020, 11, 7, 3, 30)
        self.dwd_weather.get_timeframe_condition(test_time, 3, False)
        mock_update.assert_not_called()

    def test_not_in_timerange(self):
        test_time = datetime(2000, 11, 7, 3, 30)
        self.assertIsNone(self.dwd_weather.get_timeframe_condition(test_time, 3))

    @patch("simple_dwd_weatherforecast.dwdforecast.Weather.update", return_value=None)
    def test_part_in_timerange(self, _):
        test_time = datetime(2020, 11, 6, 1, 0)
        self.assertEqual(
            self.dwd_weather.get_timeframe_condition(test_time, 6),
            "cloudy",
        )

    @patch("simple_dwd_weatherforecast.dwdforecast.Weather.update", return_value=None)
    def test_49_max(self, _):
        test_time = datetime(2020, 11, 6, 10, 0)
        self.assertEqual(
            self.dwd_weather.get_timeframe_condition(test_time, 3),
            "partlycloudy",
        )

    @patch("simple_dwd_weatherforecast.dwdforecast.Weather.update", return_value=None)
    def test_75_max(self, _):
        test_time = datetime(2020, 11, 7, 10, 0)
        self.assertEqual(
            self.dwd_weather.get_timeframe_condition(test_time, 6),
            "sunny",
        )

    @patch("simple_dwd_weatherforecast.dwdforecast.Weather.update", return_value=None)
    def test_3_max(self, _):
        test_time = datetime(2020, 11, 16, 9, 0)
        self.assertEqual(
            self.dwd_weather.get_timeframe_condition(test_time, 3),
            "cloudy",
        )

    @patch("simple_dwd_weatherforecast.dwdforecast.Weather.update", return_value=None)
    def test_hourly_timeframe(self, _):
        test_time = datetime(2020, 11, 6, 4, 0)
        self.assertEqual(
            self.dwd_weather.get_timeframe_condition(test_time, 1),
            "partlycloudy",
        )
        test_time = test_time + timedelta(hours=1)
        self.assertEqual(
            self.dwd_weather.get_timeframe_condition(test_time, 1),
            "cloudy",
        )
        test_time = test_time + timedelta(hours=1)
        self.assertEqual(
            self.dwd_weather.get_timeframe_condition(test_time, 1),
            "sunny",
        )
        test_time = test_time + timedelta(hours=1)
        self.assertEqual(
            self.dwd_weather.get_timeframe_condition(test_time, 1),
            "fog",
        )
