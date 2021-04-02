import unittest
from simple_dwd_weatherforecast import dwdforecast
from tests.dummy_data import parsed_data


class KMLParseTestCase(unittest.TestCase):
    def setUp(self):
        self.dwd_weather = dwdforecast.Weather("H889")

    def test_parse_kml(self):
        in_file = open("TEST_N4333.kml", "rb")
        data = in_file.read()
        in_file.close()
        self.dwd_weather.parse_kml(data)
        self.assertEqual(self.dwd_weather.forecast_data, parsed_data)
