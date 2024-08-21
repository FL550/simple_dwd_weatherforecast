import unittest
from simple_dwd_weatherforecast import dwdforecast
from dummy_data import parsed_data


class WeatherInit(unittest.TestCase):
    def setUp(self):
        self.dwd_weather = dwdforecast.Weather("L821")
        self.dwd_weather.forecast_data = parsed_data  # type: ignore

    def test_init_with_wrong_id(self):
        with self.assertRaises(ValueError) as _:
            dwdforecast.Weather("H89")

    def test_init_with_number(self):
        with self.assertRaises(ValueError) as _:
            dwdforecast.Weather(42)

    def test_init_with_no_id(self):
        with self.assertRaises(TypeError) as _:
            dwdforecast.Weather()  # type: ignore

    def test_uv_index(self):
        self.assertEqual(self.dwd_weather.nearest_uv_index_station, "10637")
