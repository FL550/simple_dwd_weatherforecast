import unittest
from datetime import datetime
from simple_dwd_weatherforecast import dwdforecast
from dummy_data import parsed_data


class Weather_is_in_timerange(unittest.TestCase):
    def setUp(self):
        self.dwd_weather = dwdforecast.Weather("H889")
        self.dwd_weather.forecast_data = parsed_data  # type: ignore

    def test_is_in_timerange(self):
        test_time = datetime(2020, 11, 7, 3, 30)
        self.assertTrue(self.dwd_weather.is_in_timerange(test_time))

    def test_is_in_timerange_past(self):
        test_time = datetime(2000, 11, 5, 17, 30)
        self.assertFalse(self.dwd_weather.is_in_timerange(test_time))

    def test_is_in_timerange_future(self):
        test_time = datetime(2102, 11, 5, 7, 30)
        self.assertFalse(self.dwd_weather.is_in_timerange(test_time))

    def test_is_in_timerange_day(self):
        test_time = datetime(2020, 11, 6, 0, 0)
        self.assertTrue(self.dwd_weather.is_in_timerange_day(test_time))

    def test_is_in_timerange_day_past(self):
        test_time = datetime(2000, 11, 5, 17, 30)
        self.assertFalse(self.dwd_weather.is_in_timerange(test_time))

    def test_is_in_timerange_day_future(self):
        test_time = datetime(2102, 11, 5, 7, 30)
        self.assertFalse(self.dwd_weather.is_in_timerange(test_time))
