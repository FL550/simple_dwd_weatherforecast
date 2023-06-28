import unittest
from simple_dwd_weatherforecast import dwdmap


class MapTestCase(unittest.TestCase):
    def test_prevent_too_large_height(self):
        with self.assertRaises(ValueError):
            dwdmap.get_map(4.4, 46.4, 16.1, 55.6, dwdmap.WeatherMapType.NIEDERSCHLAGSRADAR, dwdmap.WeatherBackgroundMapType.BUNDESLAENDER, 1300, 700)

    def test_prevent_too_large_width(self):
        with self.assertRaises(ValueError):
            dwdmap.get_map(4.4, 46.4, 16.1, 55.6, dwdmap.WeatherMapType.NIEDERSCHLAGSRADAR, dwdmap.WeatherBackgroundMapType.BUNDESLAENDER, 300, 1700)

    def test_prevent_too_large(self):
        with self.assertRaises(ValueError):
            dwdmap.get_map(4.4, 46.4, 16.1, 55.6, dwdmap.WeatherMapType.NIEDERSCHLAGSRADAR, dwdmap.WeatherBackgroundMapType.BUNDESLAENDER, 1300, 1700)
