import unittest
from simple_dwd_weatherforecast import dwdforecast
from dummy_data import parsed_data


class Weather_get_station_name(unittest.TestCase):
    def setUp(self):
        self.dwd_weather = dwdforecast.Weather("H889")
        self.dwd_weather.forecast_data = parsed_data  # type: ignore

    def test_get_station_name(self):
        self.assertEqual(self.dwd_weather.get_station_name(), "Burbach-Wuergendorf")
