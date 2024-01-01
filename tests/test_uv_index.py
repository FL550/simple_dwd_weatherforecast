import unittest
from simple_dwd_weatherforecast import dwdforecast
from dummy_uv import parsed_data


class UvIndexTestCase(unittest.TestCase):
    def setUp(self):
        self.dwd_weather = dwdforecast.Weather("L821")
        self.dwd_weather.uv_reports = parsed_data

    def test_uv_today(self):
        self.assertEqual(self.dwd_weather.get_uv_index(0), 0)

    def test_uv_tomorrow(self):
        self.assertEqual(self.dwd_weather.get_uv_index(1), 1)

    def test_uv_dayafter_tomorrow(self):
        self.assertEqual(self.dwd_weather.get_uv_index(2), 2)
