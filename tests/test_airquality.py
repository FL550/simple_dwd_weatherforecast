from simple_dwd_weatherforecast.dwdforecast import AirQuality
import csv
import unittest
from unittest.mock import patch
from datetime import datetime


class AirQualityTestParsingHourly(unittest.TestCase):
    def setUp(self):
        self.station = AirQuality("", "hourly")
        with open("tests/lq_forecast_2025122409.csv", encoding="utf-8") as f:
            content = f.read()
            content = csv.DictReader(content.splitlines(), delimiter=";")
            self.data = self.station._parse_hourly(content)

    def test_count(self):
        assert len(self.data) == 442

    def test_count_stations(self):
        assert len(self.data["DEBE056"]) == 97

    def test_firstentry(self):
        assert self.data["DERP011"][1] == {
            "Stickstoffdioxid": 7.4,
            "Ozon": 55.4,
            "PM10": 73.1,
            "PM2_5": 53.3,
            "Gleitendes 24h Mittel PM10": 33.5,
            "Gleitendes 24h Mittel PM2_5": 16.8,
        }
        assert self.data["DEBE056"][1] == {
            "Stickstoffdioxid": 1.7,
            "Ozon": None,
            "PM10": None,
            "PM2_5": 6.9,
            "Gleitendes 24h Mittel PM10": None,
            "Gleitendes 24h Mittel PM2_5": 8.6,
        }

    def test_lastentry(self):
        assert self.data["DEBE056"][96] == {
            "Stickstoffdioxid": 17.0,
            "Ozon": None,
            "PM10": None,
            "PM2_5": 8.3,
            "Gleitendes 24h Mittel PM10": None,
            "Gleitendes 24h Mittel PM2_5": 12.0,
        }


class AirQualityTestParsingDaily(unittest.TestCase):
    def setUp(self):
        self.station = AirQuality("", "daily")
        with open("tests/lq_average_allstats_2025122409.csv", encoding="utf-8") as f:
            content = f.read()
            content = csv.DictReader(content.splitlines(), delimiter=";")
            self.data = self.station._parse_daily(content)

    def test_count(self):
        assert len(self.data) == 442

    def test_station(self):
        assert self.data["DEBE056"] == {
            "today": {
                "Stickstoffdioxid": "   9.9",
                "Ozon": None,
                "PM10": None,
                "PM2_5": "  21.1",
            },
            "tomorrow": {
                "Stickstoffdioxid": "  25.0",
                "Ozon": None,
                "PM10": None,
                "PM2_5": "  19.4",
            },
            "day_after": {
                "Stickstoffdioxid": "  18.1",
                "Ozon": None,
                "PM10": None,
                "PM2_5": "  13.3",
            },
        }


class AirQualityTestGetStationFromLocation(unittest.TestCase):
    def test_get_station(self):
        station = AirQuality.get_station_from_location(50.536266, 9.975635, "daily")
        assert station.station_id == "DEHE051"
        station = AirQuality.get_station_from_location(53.092022, 8.127382, "hourly")
        assert station.station_id == "DENI143"
