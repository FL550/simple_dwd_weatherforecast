import unittest
from datetime import datetime
from simple_dwd_weatherforecast import dwdforecast
from dummy_data import parsed_data


class Weather_get_timeframe_values(unittest.TestCase):
    def setUp(self):
        self.dwd_weather = dwdforecast.Weather("H889")
        self.dwd_weather.forecast_data = parsed_data  # type: ignore

    def test_timeframe_6(self):
        test_time = datetime(2020, 11, 7, 1, 0)
        test_data = [
            {
                "TTT": 274.55,
                "Td": 273.15,
                "condition": "75",
                "PPPP": 103030.0,
                "DD": 52.0,
                "FF": 1.54,
                "FX1": 2.57,
                "RR1c": 6.54,
                "wwP": 3.0,
                "DRR1": 0.0,
                "N": 24.0,
                "PEvap": None,
                "VV": 12900.0,
                "SunD1": 0.0,
                "Rad1h": None,
                "wwM": 2.0,
                "humidity": 90.4,
            },
            {
                "TTT": 274.35,
                "Td": 273.15,
                "condition": "0",
                "PPPP": 103010.0,
                "DD": 52.0,
                "FF": 1.54,
                "FX1": 2.57,
                "RR1c": 5.43,
                "wwP": 1.0,
                "DRR1": 0.0,
                "N": 28.0,
                "PEvap": None,
                "VV": 12200.0,
                "SunD1": 0.0,
                "Rad1h": None,
                "wwM": 3.0,
                "humidity": 91.7,
            },
            {
                "TTT": 274.35,
                "Td": 273.25,
                "condition": "0",
                "PPPP": 103000.0,
                "DD": 53.0,
                "FF": 1.54,
                "FX1": 2.57,
                "RR1c": 0.0,
                "wwP": 1.0,
                "DRR1": 0.0,
                "N": 31.0,
                "PEvap": None,
                "VV": 10900.0,
                "SunD1": 0.0,
                "Rad1h": None,
                "wwM": 5.0,
                "humidity": 92.4,
            },
            {
                "TTT": 274.35,
                "Td": 273.35,
                "condition": "0",
                "PPPP": 102970.0,
                "DD": 51.0,
                "FF": 1.54,
                "FX1": 3.09,
                "RR1c": 0.0,
                "wwP": 1.0,
                "DRR1": 0.0,
                "N": 35.0,
                "PEvap": None,
                "VV": 9600.0,
                "SunD1": 0.0,
                "Rad1h": None,
                "wwM": 6.0,
                "humidity": 93.0,
            },
            {
                "TTT": 274.55,
                "Td": 273.45,
                "condition": "0",
                "PPPP": 102950.0,
                "DD": 53.0,
                "FF": 1.54,
                "FX1": 3.09,
                "RR1c": 0.0,
                "wwP": 2.0,
                "DRR1": 0.0,
                "N": 40.0,
                "PEvap": None,
                "VV": 8700.0,
                "SunD1": 0.0,
                "Rad1h": None,
                "wwM": 6.0,
                "humidity": 92.4,
            },
            {
                "TTT": 274.85,
                "Td": 273.55,
                "condition": "0",
                "PPPP": 102950.0,
                "DD": 64.0,
                "FF": 1.54,
                "FX1": 3.09,
                "RR1c": 0.0,
                "wwP": 2.0,
                "DRR1": 0.0,
                "N": 41.0,
                "PEvap": 0.4,
                "VV": 8000.0,
                "SunD1": 0.0,
                "Rad1h": None,
                "wwM": 6.0,
                "humidity": 91.1,
            },
        ]

        self.assertEqual(
            self.dwd_weather.get_timeframe_values(test_time, 6),
            test_data,
        )

    def test_timeframe_3(self):
        test_time = datetime(2020, 11, 7, 3, 0)
        test_data = [
            {
                "TTT": 274.35,
                "Td": 273.25,
                "condition": "0",
                "PPPP": 103000.0,
                "DD": 53.0,
                "FF": 1.54,
                "FX1": 2.57,
                "RR1c": 0.0,
                "wwP": 1.0,
                "DRR1": 0.0,
                "N": 31.0,
                "PEvap": None,
                "VV": 10900.0,
                "SunD1": 0.0,
                "Rad1h": None,
                "wwM": 5.0,
                "humidity": 92.4,
            },
            {
                "TTT": 274.35,
                "Td": 273.35,
                "condition": "0",
                "PPPP": 102970.0,
                "DD": 51.0,
                "FF": 1.54,
                "FX1": 3.09,
                "RR1c": 0.0,
                "wwP": 1.0,
                "DRR1": 0.0,
                "N": 35.0,
                "PEvap": None,
                "VV": 9600.0,
                "SunD1": 0.0,
                "Rad1h": None,
                "wwM": 6.0,
                "humidity": 93.0,
            },
            {
                "TTT": 274.55,
                "Td": 273.45,
                "condition": "0",
                "PPPP": 102950.0,
                "DD": 53.0,
                "FF": 1.54,
                "FX1": 3.09,
                "RR1c": 0.0,
                "wwP": 2.0,
                "DRR1": 0.0,
                "N": 40.0,
                "PEvap": None,
                "VV": 8700.0,
                "SunD1": 0.0,
                "Rad1h": None,
                "wwM": 6.0,
                "humidity": 92.4,
            },
        ]

        self.assertEqual(
            self.dwd_weather.get_timeframe_values(test_time, 3),
            test_data,
        )

    def test_timeframe_empty(self):
        test_time = datetime(2020, 10, 7, 1, 0)
        test_data = []

        self.assertEqual(
            self.dwd_weather.get_timeframe_values(test_time, 6),
            test_data,
        )

    def test_timeframe_part(self):
        test_time = datetime(2020, 11, 6, 0, 0)
        test_data = [
            {
                "TTT": 272.95,
                "Td": 272.65,
                "condition": "2",
                "PPPP": 103640.0,
                "DD": 50.0,
                "FF": 1.54,
                "FX1": 3.09,
                "RR1c": 0.01,
                "wwP": 2.0,
                "DRR1": 0.0,
                "N": 35.0,
                "PEvap": None,
                "VV": 8000.0,
                "SunD1": 0.0,
                "Rad1h": None,
                "wwM": 8.0,
                "humidity": 97.8,
            },
            {
                "TTT": 273.05,
                "Td": 272.45,
                "condition": "3",
                "PPPP": 103620.0,
                "DD": 52.0,
                "FF": 1.54,
                "FX1": 3.6,
                "RR1c": 0.12,
                "wwP": 3.0,
                "DRR1": 0.0,
                "N": 36.0,
                "PEvap": None,
                "VV": 6400.0,
                "SunD1": 0.0,
                "Rad1h": None,
                "wwM": 9.0,
                "humidity": 95.7,
            },
        ]

        self.assertEqual(
            self.dwd_weather.get_timeframe_values(test_time, 6),
            test_data,
        )
