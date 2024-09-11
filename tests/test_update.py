import unittest
from unittest.mock import patch
from simple_dwd_weatherforecast import dwdforecast
from dummy_data import parsed_data
from datetime import datetime, timezone
import time


class WeatherUpdate(unittest.TestCase):
    def setUp(self):
        self.dwd_weather = dwdforecast.Weather("H889")
        self.dwd_weather.forecast_data = parsed_data  # type: ignore

    @patch(
        "simple_dwd_weatherforecast.dwdforecast.Weather.download_latest_report",
        return_value=None,
    )
    @patch(
        "simple_dwd_weatherforecast.dwdforecast.Weather.download_weather_report",
        return_value=None,
    )
    def test_download(self, _1, _2):
        self.dwd_weather.update()
        self.assertIsNotNone(self.dwd_weather.forecast_data)
        self.assertIsNotNone(self.dwd_weather.forecast_data)
        self.assertEqual(self.dwd_weather.station_id, "H889")
        self.assertEqual(self.dwd_weather.issue_time.date(), datetime.now().date())  # type: ignore

    @patch(
        "simple_dwd_weatherforecast.dwdforecast.Weather.download_latest_report",
        return_value=None,
    )
    @patch(
        "simple_dwd_weatherforecast.dwdforecast.Weather.download_weather_report",
        return_value=None,
    )
    @patch(
        "simple_dwd_weatherforecast.dwdforecast.Weather.download_latest_kml",
        return_value=None,
    )
    def test_issue_time_none(self, mock_function, _1, _2):
        self.dwd_weather.update()
        mock_function.assert_called()

    @patch(
        "simple_dwd_weatherforecast.dwdforecast.Weather.download_latest_report",
        return_value=None,
    )
    @patch(
        "simple_dwd_weatherforecast.dwdforecast.Weather.download_weather_report",
        return_value=None,
    )
    @patch(
        "simple_dwd_weatherforecast.dwdforecast.Weather.download_latest_kml",
        return_value=None,
    )
    def test_issue_time_old(self, mock_function, _1, _2):
        self.dwd_weather.issue_time = datetime(
            *(time.strptime("2020-11-06T03:00:00.000Z", "%Y-%m-%dT%H:%M:%S.%fZ")[0:6]),
            0,
            timezone.utc,
        )
        self.dwd_weather.update()
        mock_function.assert_called()

    @patch(
        "simple_dwd_weatherforecast.dwdforecast.Weather.download_latest_report",
        return_value=None,
    )
    @patch(
        "simple_dwd_weatherforecast.dwdforecast.Weather.download_weather_report",
        return_value=None,
    )
    @patch(
        "simple_dwd_weatherforecast.dwdforecast.Weather.download_latest_kml",
        return_value=None,
    )
    @patch(
        "simple_dwd_weatherforecast.dwdforecast.Weather.parse_kml", return_value=None
    )
    def test_issue_time_actual(self, mock_parse_kml, _1, _2, _3):
        self.dwd_weather.issue_time = datetime.now(timezone.utc)
        self.dwd_weather.update()
        mock_parse_kml.assert_not_called()


class WeatherDownload(unittest.TestCase):
    @patch(
        "simple_dwd_weatherforecast.dwdforecast.Weather.parse_kml", return_value=None
    )
    def test_etag_valid(self, mock_function):
        stationid = "H889"
        self.dwd_weather = dwdforecast.Weather(stationid)
        self.dwd_weather.etags = {}
        self.dwd_weather.download_latest_kml(stationid)
        self.dwd_weather.download_latest_kml(stationid)
        mock_function.assert_called_once()

    @patch(
        "simple_dwd_weatherforecast.dwdforecast.Weather.parse_kml", return_value=None
    )
    def test_etag_invalid(self, mock_function):
        stationid = "H889"
        self.dwd_weather = dwdforecast.Weather(stationid)
        self.dwd_weather.etags = {}
        self.dwd_weather.etags[
            "https://opendata.dwd.de/weather/local_forecasts/mos/MOSMIX_L/single_stations/{stationid}/kml/MOSMIX_L_LATEST_{stationid}.kmz"
        ] = "invalid_etag"
        self.dwd_weather.download_latest_kml(stationid)
        mock_function.assert_called()

    @patch(
        "simple_dwd_weatherforecast.dwdforecast.Weather.parse_kml", return_value=None
    )
    def test_etag_missing(self, mock_function):
        stationid = "H889"
        self.dwd_weather = dwdforecast.Weather(stationid)
        self.dwd_weather.etags = {}
        self.dwd_weather.download_latest_kml(stationid)
        mock_function.assert_called()

    @patch(
        "simple_dwd_weatherforecast.dwdforecast.Weather.download_latest_report",
        return_value=None,
    )
    @patch(
        "simple_dwd_weatherforecast.dwdforecast.Weather.download_weather_report",
        return_value=None,
    )
    @patch(
        "simple_dwd_weatherforecast.dwdforecast.Weather.download_latest_kml",
        return_value=None,
    )
    @patch(
        "simple_dwd_weatherforecast.dwdforecast.Weather.parse_kml", return_value=None
    )
    def test_report_not_called(self, _1, _2, _3, mock_download_latest_report):
        self.dwd_weather = dwdforecast.Weather("H889")
        self.dwd_weather.update()
        mock_download_latest_report.assert_not_called()

    @patch(
        "simple_dwd_weatherforecast.dwdforecast.Weather.download_latest_report",
        return_value=None,
    )
    @patch(
        "simple_dwd_weatherforecast.dwdforecast.Weather.download_weather_report",
        return_value=None,
    )
    @patch(
        "simple_dwd_weatherforecast.dwdforecast.Weather.download_latest_kml",
        return_value=None,
    )
    @patch(
        "simple_dwd_weatherforecast.dwdforecast.Weather.parse_kml", return_value=None
    )
    def test_measurements_called(self, _1, _2, _3, mock_download_latest_report):
        self.dwd_weather = dwdforecast.Weather("10130")
        self.dwd_weather.update(with_measurements=True)
        mock_download_latest_report.assert_called()

    @patch(
        "simple_dwd_weatherforecast.dwdforecast.Weather.download_latest_report",
        return_value=None,
    )
    @patch(
        "simple_dwd_weatherforecast.dwdforecast.Weather.download_weather_report",
        return_value=None,
    )
    @patch(
        "simple_dwd_weatherforecast.dwdforecast.Weather.download_latest_kml",
        return_value=None,
    )
    @patch(
        "simple_dwd_weatherforecast.dwdforecast.Weather.parse_kml", return_value=None
    )
    def test_weather_report_called(self, _1, _2, mock_download_weather_report, _3):
        self.dwd_weather = dwdforecast.Weather("01008")
        self.dwd_weather.region = "HH"
        self.dwd_weather.update(with_report=True)
        mock_download_weather_report.assert_called()

    @patch(
        "simple_dwd_weatherforecast.dwdforecast.Weather.download_latest_report",
        return_value=None,
    )
    @patch(
        "simple_dwd_weatherforecast.dwdforecast.Weather.download_weather_report",
        return_value=None,
    )
    @patch(
        "simple_dwd_weatherforecast.dwdforecast.Weather.download_latest_kml",
        return_value=None,
    )
    @patch(
        "simple_dwd_weatherforecast.dwdforecast.Weather.parse_kml", return_value=None
    )
    def test_weather_report_not_called(self, _1, _2, mock_download_weather_report, _3):
        self.dwd_weather = dwdforecast.Weather("01008")
        self.dwd_weather.region = None
        self.dwd_weather.update()
        mock_download_weather_report.assert_not_called()

    def test_weather_report_available(self):
        self.dwd_weather = dwdforecast.Weather("10739")
        self.dwd_weather.update(with_report=True)
        self.assertIsNotNone(self.dwd_weather.weather_report)
