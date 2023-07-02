import unittest
from simple_dwd_weatherforecast import dwdforecast


class ReportedWeatherTestCase(unittest.TestCase):
    def test_download(self):
        dwdweather = dwdforecast.Weather("01008")
        dwdweather.download_latest_report()
        self.assertIsNotNone(dwdweather.report_data)

    def test_has_report_true(self):
        dwdweather = dwdforecast.Weather("01008")
        self.assertTrue(dwdweather.has_measurement("01008"))

    def test_has_report_false(self):
        dwdweather = dwdforecast.Weather("X472")
        self.assertFalse(dwdweather.has_measurement("X472"))

    def test_has_report_invalid_station(self):
        dwdweather = dwdforecast.Weather("01008")
        self.assertFalse(dwdweather.has_measurement("01"))