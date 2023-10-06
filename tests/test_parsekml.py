import unittest
from simple_dwd_weatherforecast import dwdforecast
from dummy_data import parsed_data


class KMLParseTestCase(unittest.TestCase):
    def setUp(self):
        self.dwd_weather = dwdforecast.Weather("N4333")

    def test_parse_kml(self):
        in_file = open("development/TEST_N4333.kml", "rb")
        data = in_file.read()
        in_file.close()
        self.dwd_weather.parse_kml(data)
        self.assertEqual(self.dwd_weather.forecast_data, parsed_data)

class KMLParseFullTestCase(unittest.TestCase):
    def setUp(self):
        self.dwd_weather = dwdforecast.Weather("L511")

    def test_parse_kml(self):
        in_file = open("development/MOSMIX_S_2023091815_240.kml", "rb")
        data = in_file.read()
        in_file.close()
        self.dwd_weather.parse_kml(data)
        self.assertEqual(self.dwd_weather.forecast_data, parsed_data)
