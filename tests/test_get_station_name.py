import unittest
from unittest.mock import patch
from simple_dwd_weatherforecast import dwdforecast
from test_data import parsed_data


class Weather_get_station_name(unittest.TestCase):
    def setUp(self):
        self.dwd_weather = dwdforecast.Weather("H889")
        self.dwd_weather.forecast_data = parsed_data
        self.dwd_weather.station_name = "BAD HOMBURG"

    def test_get_station_name(self):
        self.assertEqual(self.dwd_weather.get_station_name(), "BAD HOMBURG")

    @patch("simple_dwd_weatherforecast.dwdforecast.Weather.update", return_value=None)
    def test_get_station_name_force_update(self, mock_update):
        self.dwd_weather.get_station_name(True)
        mock_update.assert_called()

    @patch("simple_dwd_weatherforecast.dwdforecast.Weather.update", return_value=None)
    def test_get_station_name_no_name_set(self, mock_update):
        self.dwd_weather.station_name = ""
        self.dwd_weather.get_station_name()
        mock_update.assert_called()
