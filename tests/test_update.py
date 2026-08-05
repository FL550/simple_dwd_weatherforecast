import unittest
from unittest.mock import Mock, patch
from simple_dwd_weatherforecast import dwdforecast
from dummy_data import parsed_data
from datetime import datetime, timezone
import time
import httpx


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

    def test_weather_report_umlauts(self):
        self.dwd_weather = dwdforecast.Weather("P0560")
        self.dwd_weather.update(with_report=True)
        self.assertIn("Wettervorhersage für Thüringen", self.dwd_weather.weather_report)

    @patch("simple_dwd_weatherforecast.dwdforecast.stream_unzip")
    @patch("simple_dwd_weatherforecast.dwdforecast.httpx.head")
    def test_download_large_kml_timeout_reports_package_error(
        self, mock_head, mock_stream_unzip
    ):
        self.dwd_weather = dwdforecast.Weather("H889")
        mock_head.return_value = Mock(status_code=200)
        mock_stream_unzip.side_effect = httpx.ReadTimeout(
            "The read operation timed out"
        )

        with self.assertRaises(dwdforecast.ForecastDownloadError) as context:
            self.dwd_weather.download_large_kml("H889")

        self.assertIn(
            "Timed out while downloading hourly forecast data for station H889.",
            str(context.exception),
        )

    @patch("simple_dwd_weatherforecast.dwdforecast.httpx.head")
    def test_download_large_kml_head_timeout_reports_package_error(self, mock_head):
        self.dwd_weather = dwdforecast.Weather("H889")
        mock_head.side_effect = httpx.ReadTimeout("The read operation timed out")

        with self.assertRaises(dwdforecast.ForecastDownloadError) as context:
            self.dwd_weather.download_large_kml("H889")

        self.assertIn(
            "Timed out while checking hourly forecast data from DWD.",
            str(context.exception),
        )

    @patch("simple_dwd_weatherforecast.dwdforecast.httpx.get")
    def test_download_small_kml_timeout_reports_package_error(self, mock_get):
        self.dwd_weather = dwdforecast.Weather("H889")
        mock_get.side_effect = httpx.ReadTimeout("The read operation timed out")

        with self.assertRaises(dwdforecast.ForecastDownloadError) as context:
            self.dwd_weather.download_small_kml("H889")

        self.assertIn(
            "Timed out while downloading forecast data for station H889.",
            str(context.exception),
        )

    @patch("simple_dwd_weatherforecast.dwdforecast.httpx.get")
    def test_download_small_kml_http_error_reports_package_error(self, mock_get):
        self.dwd_weather = dwdforecast.Weather("H889")
        mock_get.side_effect = httpx.HTTPStatusError(
            "Request failed",
            request=httpx.Request("GET", "https://example.com"),
            response=httpx.Response(status_code=500),
        )

        with self.assertRaises(dwdforecast.ForecastDownloadError) as context:
            self.dwd_weather.download_small_kml("H889")

        self.assertIn(
            "Failed to download forecast data for station H889.",
            str(context.exception),
        )
