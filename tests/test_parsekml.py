from datetime import datetime, timezone
import unittest
from unittest.mock import patch

from simple_dwd_weatherforecast import dwdforecast
import dummy_data
import dummy_data_full


class KMLParseTestCase(unittest.TestCase):
    FILE_NAME = "development/TEST_N4333.kml"

    def setUp(self):
        self.dwd_weather = dwdforecast.Weather("N4333")

    def test_parse_kml(self):
        with open(self.FILE_NAME, "rb") as kml:
            self.dwd_weather.parse_kml(kml.read())
            self.assertEqual(self.dwd_weather.forecast_data, dummy_data.parsed_data)
            self.assertEqual(
                self.dwd_weather.issue_time,
                datetime(2020, 11, 6, 3, 0, tzinfo=timezone.utc),
            )


def helper(file):
    # Iterable that yields the bytes of a zip file
    with open(file, "rb") as kml:
        content = kml.read()
        while len(content) > 0:
            yield content
            content = kml.read()


class KMLParseFullTestCase(unittest.TestCase):
    FILE_NAME = "development/MOSMIX_L_2023100809_stripped.kmz"

    def setUp(self):
        self.dwd_weather = dwdforecast.Weather("L511")

    @patch(
        "simple_dwd_weatherforecast.dwdforecast.Weather.get_chunks",
        return_value=helper(FILE_NAME),
    )
    def test_parse_kml(self, _):
        self.dwd_weather.download_latest_kml(
            self.dwd_weather.station_id, force_hourly=True
        )
        self.assertEqual(self.dwd_weather.forecast_data, dummy_data_full.parsed_data)
