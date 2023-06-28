import unittest
from unittest.mock import patch
from datetime import datetime
from simple_dwd_weatherforecast import dwdforecast
from dummy_data import parsed_data


class Weather_get_forecast_condition(unittest.TestCase):
    def setUp(self):
        self.dwd_weather = dwdforecast.Weather("H889")
        self.dwd_weather.forecast_data = parsed_data
        self.dwd_weather.station_name = "BAD HOMBURG"

    @patch("simple_dwd_weatherforecast.dwdforecast.Weather.update", return_value=None)
    def test_shouldupdate(self, mock_update):
        test_time = datetime(2020, 11, 7, 3, 30)
        self.dwd_weather.get_forecast_condition(test_time, True)
        mock_update.assert_called()

    @patch("simple_dwd_weatherforecast.dwdforecast.Weather.update", return_value=None)
    def test_shouldupdate_not(self, mock_update):
        test_time = datetime(2020, 11, 7, 3, 30)
        self.dwd_weather.get_forecast_condition(test_time, False)
        mock_update.assert_not_called()

    def test_not_in_timerange(self):
        test_time = datetime(2000, 11, 7, 3, 30)
        self.assertIsNone(self.dwd_weather.get_forecast_condition(test_time))

    @patch("simple_dwd_weatherforecast.dwdforecast.Weather.update", return_value=None)
    def test_hour_on(self, _):
        test_time = datetime(2020, 11, 6, 6, 0)
        self.assertEqual(
            self.dwd_weather.get_forecast_condition(test_time),
            "sunny",
        )

    @patch("simple_dwd_weatherforecast.dwdforecast.Weather.update", return_value=None)
    def test_hour_last(self, _):
        test_time = datetime(2020, 11, 6, 6, 59)
        self.assertEqual(
            self.dwd_weather.get_forecast_condition(test_time),
            "sunny",
        )

    @patch("simple_dwd_weatherforecast.dwdforecast.Weather.update", return_value=None)
    def test_end_of_day(self, _):
        test_time = datetime(2020, 11, 6, 23, 59)
        self.assertEqual(
            self.dwd_weather.get_forecast_condition(test_time),
            "rainy",
        )

    @patch("simple_dwd_weatherforecast.dwdforecast.Weather.update", return_value=None)
    def test_midnight(self, _):
        test_time = datetime(2020, 11, 7)
        self.assertEqual(
            self.dwd_weather.get_forecast_condition(test_time),
            "fog",
        )

    @patch("simple_dwd_weatherforecast.dwdforecast.Weather.update", return_value=None)
    def test_after_midnight_short(self, _):
        test_time = datetime(2020, 11, 7, 0, 43)
        self.assertEqual(
            self.dwd_weather.get_forecast_condition(test_time),
            "fog",
        )

    @patch("simple_dwd_weatherforecast.dwdforecast.Weather.update", return_value=None)
    def test_after_midnight_longer(self, _):
        test_time = datetime(2020, 11, 7, 1, 43)
        self.assertEqual(
            self.dwd_weather.get_forecast_condition(test_time),
            "snowy",
        )
