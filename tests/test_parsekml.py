import unittest
from zipfile import ZipFile

from simple_dwd_weatherforecast import dwdforecast
from dummy_data import parsed_data


class KMLParseTestCase(unittest.TestCase):
    FILE_NAME = "development/TEST_N4333.kml"
    
    def setUp(self):
        self.dwd_weather = dwdforecast.Weather("N4333")

    def test_parse_kml(self):
        with open(self.FILE_NAME, "rb") as kml:
            self.dwd_weather.parse_kml(kml)
            self.assertEqual(self.dwd_weather.forecast_data, parsed_data)


class KMLParseFullTestCase(unittest.TestCase):
    FILE_NAME = "development/MOSMIX_S_LATEST_240.kmz"
    
    def setUp(self):
        self.dwd_weather = dwdforecast.Weather("L511")

    def test_parse_kml(self):
        with open(self.FILE_NAME, 'rb') as f:
            with ZipFile(f, 'r') as zip_file:
                with zip_file.open(zip_file.namelist()[0], "r") as kml:
                    self.dwd_weather.parse_kml(kml)
                    self.assertEqual(self.dwd_weather.forecast_data, parsed_data)
