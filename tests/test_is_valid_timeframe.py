import unittest
from simple_dwd_weatherforecast import dwdforecast
from dummy_data import parsed_data


class Weather_is_valid_timeframe(unittest.TestCase):
    def setUp(self):
        self.dwd_weather = dwdforecast.Weather("H889")
        self.dwd_weather.forecast_data = parsed_data  # type: ignore

    def test_is_day(self):
        self.assertTrue(self.dwd_weather.is_valid_timeframe(24))

    def test_is_half_day(self):
        self.assertTrue(self.dwd_weather.is_valid_timeframe(12))

    def test_is_too_large(self):
        self.assertFalse(self.dwd_weather.is_valid_timeframe(25))

    def test_remainder_not_zero(self):
        self.assertFalse(self.dwd_weather.is_valid_timeframe(5))

    def test_is_zero(self):
        self.assertFalse(self.dwd_weather.is_valid_timeframe(0))

    def test_is_negative(self):
        self.assertFalse(self.dwd_weather.is_valid_timeframe(-5))
