from simple_dwd_weatherforecast.dwdforecast import WeatherDataType
import unittest
from unittest.mock import patch
from datetime import datetime
from simple_dwd_weatherforecast import dwdforecast
from dummy_data import parsed_data


class Weather_get_daily_avg(unittest.TestCase):
    def setUp(self):
        self.dwd_weather = dwdforecast.Weather("H889")
        self.dwd_weather.forecast_data = parsed_data
        self.dwd_weather.station_name = "BAD HOMBURG"

    @patch("simple_dwd_weatherforecast.dwdforecast.Weather.update", return_value=None)
    def test_shouldupdate(self, mock_update):
        test_time = datetime(2020, 11, 7, 3, 30)
        self.dwd_weather.get_daily_avg(WeatherDataType.PRECIPITATION, test_time, True)
        mock_update.assert_called()

    @patch("simple_dwd_weatherforecast.dwdforecast.Weather.update", return_value=None)
    def test_shouldupdate_not(self, mock_update):
        test_time = datetime(2020, 11, 7, 3, 30)
        self.dwd_weather.get_daily_avg(WeatherDataType.PRECIPITATION, test_time, False)
        mock_update.assert_not_called()

    def test_not_in_timerange(self):
        test_time = datetime(2000, 11, 7, 3, 30)
        self.assertIsNone(
            self.dwd_weather.get_daily_avg(WeatherDataType.PRECIPITATION, test_time)
        )

    @patch("simple_dwd_weatherforecast.dwdforecast.Weather.update", return_value=None)
    def test_precipitation(self, mock_update):
        test_time = datetime(2020, 11, 6, 12, 0)
        print(self.dwd_weather.get_day_values(test_time))
        self.assertEqual(
            self.dwd_weather.get_daily_avg(WeatherDataType.PRECIPITATION, test_time),
            1.8,
        )

    @patch("simple_dwd_weatherforecast.dwdforecast.Weather.update", return_value=None)
    def test_temperature(self, mock_update):
        test_time = datetime(2020, 11, 6, 23, 0)
        self.assertEqual(
            self.dwd_weather.get_daily_avg(WeatherDataType.TEMPERATURE, test_time),
            278.09,
        )

    @patch("simple_dwd_weatherforecast.dwdforecast.Weather.update", return_value=None)
    def test_midnight(self, mock_update):
        test_time = datetime(2020, 11, 6, 0, 0)
        self.assertEqual(
            self.dwd_weather.get_daily_avg(WeatherDataType.TEMPERATURE, test_time),
            278.09,
        )
