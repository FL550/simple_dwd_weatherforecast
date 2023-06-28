from simple_dwd_weatherforecast.dwdforecast import WeatherDataType
import unittest
from unittest.mock import patch
from datetime import datetime
from simple_dwd_weatherforecast import dwdforecast
from dummy_data import parsed_data


class Weather_get_timeframe_min(unittest.TestCase):
    def setUp(self):
        self.dwd_weather = dwdforecast.Weather("H889")
        self.dwd_weather.forecast_data = parsed_data
        self.dwd_weather.station_name = "BAD HOMBURG"

    @patch("simple_dwd_weatherforecast.dwdforecast.Weather.update", return_value=None)
    def test_shouldupdate(self, mock_update):
        test_time = datetime(2020, 11, 7, 3, 30)
        self.dwd_weather.get_timeframe_min(
            WeatherDataType.PRECIPITATION, test_time, 3, True
        )
        mock_update.assert_called()

    @patch("simple_dwd_weatherforecast.dwdforecast.Weather.update", return_value=None)
    def test_shouldupdate_not(self, mock_update):
        test_time = datetime(2020, 11, 7, 3, 30)
        self.dwd_weather.get_timeframe_min(
            WeatherDataType.PRECIPITATION, test_time, 3, False
        )
        mock_update.assert_not_called()

    def test_not_in_timerange(self):
        test_time = datetime(2000, 11, 7, 3, 30)
        self.assertIsNone(
            self.dwd_weather.get_timeframe_min(
                WeatherDataType.PRECIPITATION, test_time, 3
            )
        )

    @patch("simple_dwd_weatherforecast.dwdforecast.Weather.update", return_value=None)
    def test_part_in_timerange(self, _):
        test_time = datetime(2020, 11, 6, 0, 0)
        self.assertEqual(
            self.dwd_weather.get_timeframe_min(
                WeatherDataType.TEMPERATURE, test_time, 6
            ),
            272.95,
        )

    @patch("simple_dwd_weatherforecast.dwdforecast.Weather.update", return_value=None)
    def test_precipitation(self, _):
        test_time = datetime(2020, 11, 6, 4, 0)
        self.assertEqual(
            self.dwd_weather.get_timeframe_min(
                WeatherDataType.PRECIPITATION, test_time, 3
            ),
            0.01,
        )

    @patch("simple_dwd_weatherforecast.dwdforecast.Weather.update", return_value=None)
    def test_temperature(self, _):
        test_time = datetime(2020, 11, 6, 4, 0)
        self.assertEqual(
            self.dwd_weather.get_timeframe_min(
                WeatherDataType.TEMPERATURE, test_time, 3
            ),
            272.95,
        )
