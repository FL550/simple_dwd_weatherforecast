from simple_dwd_weatherforecast.dwdforecast import WeatherDataType
import unittest
from unittest.mock import patch
from datetime import datetime
from simple_dwd_weatherforecast import dwdforecast
from test_data import parsed_data


class WeatherInit(unittest.TestCase):

    dwd_weather = dwdforecast.Weather("H889")
    dwd_weather.forecast_data = parsed_data
    dwd_weather.station_name = "BAD HOMBURG"

    def test_init_with_wrong_id(self):
        with self.assertRaises(ValueError) as _cm:
            dwdforecast.Weather("H89")

    def test_init_with_number(self):
        with self.assertRaises(ValueError) as _cm:
            dwdforecast.Weather(42)

    def test_init_with_no_id(self):
        with self.assertRaises(TypeError) as _cm:
            dwdforecast.Weather()


class Weather_get_station_name(unittest.TestCase):

    dwd_weather = dwdforecast.Weather("H889")
    dwd_weather.forecast_data = parsed_data
    dwd_weather.station_name = "BAD HOMBURG"

    def test_get_station_name(self):
        self.assertEqual(self.dwd_weather.get_station_name(), "BAD HOMBURG")

    @patch("simple_dwd_weatherforecast.dwdforecast.Weather.update", return_value=None)
    def test_get_station_name_force_update(self, mock_update):
        self.dwd_weather.get_station_name(True)
        mock_update.assert_called()

    @patch("simple_dwd_weatherforecast.dwdforecast.Weather.update", return_value=None)
    def test_get_station_name_no_name_set(self, mock_update):
        self.dwd_weather.station_name = ""
        self.dwd_weather.get_station_name()
        mock_update.assert_called()


class Weather_is_in_timerange(unittest.TestCase):

    dwd_weather = dwdforecast.Weather("H889")
    dwd_weather.forecast_data = parsed_data
    dwd_weather.station_name = "BAD HOMBURG"

    def test_is_in_timerange(self):
        test_time = datetime(2020, 11, 7, 3, 30)
        self.assertTrue(self.dwd_weather.is_in_timerange(test_time))

    def test_is_in_timerange_past(self):
        test_time = datetime(2000, 11, 5, 17, 30)
        self.assertFalse(self.dwd_weather.is_in_timerange(test_time))

    def test_is_in_timerange_future(self):
        test_time = datetime(2102, 11, 5, 7, 30)
        self.assertFalse(self.dwd_weather.is_in_timerange(test_time))


class Weather_get_forecast_data(unittest.TestCase):

    dwd_weather = dwdforecast.Weather("H889")
    dwd_weather.forecast_data = parsed_data
    dwd_weather.station_name = "BAD HOMBURG"

    @patch("simple_dwd_weatherforecast.dwdforecast.Weather.update", return_value=None)
    def test_get_forecast_data_shouldupdate(self, mock_update):
        test_time = datetime(2020, 11, 7, 3, 30)
        self.dwd_weather.get_forecast_data(
            WeatherDataType.PRECIPITATION, test_time, True
        )
        mock_update.assert_called()

    def test_get_forecast_data_not_in_timerange(self):
        test_time = datetime(2000, 11, 7, 3, 30)
        self.assertIsNone(
            self.dwd_weather.get_forecast_data(
                WeatherDataType.PRECIPITATION,
                test_time))

    @patch("simple_dwd_weatherforecast.dwdforecast.Weather.update", return_value=None)
    def test_get_forecast_data_hour_on(self, mock_update):
        test_time = datetime(2020, 11, 6, 6, 0)
        self.assertEqual(
            self.dwd_weather.get_forecast_data(
                WeatherDataType.PRECIPITATION, test_time
            ),
            1.23,
        )

    @patch("simple_dwd_weatherforecast.dwdforecast.Weather.update", return_value=None)
    def test_get_forecast_data_hour_last(self, mock_update):
        test_time = datetime(2020, 11, 6, 6, 59)
        self.assertEqual(
            self.dwd_weather.get_forecast_data(
                WeatherDataType.PRECIPITATION, test_time
            ),
            1.23,
        )

    @patch("simple_dwd_weatherforecast.dwdforecast.Weather.update", return_value=None)
    def test_get_forecast_data_end_of_day(self, mock_update):
        test_time = datetime(2020, 11, 6, 23, 59)
        self.assertEqual(
            self.dwd_weather.get_forecast_data(
                WeatherDataType.PRECIPITATION, test_time
            ),
            8.76,
        )

    @patch("simple_dwd_weatherforecast.dwdforecast.Weather.update", return_value=None)
    def test_get_forecast_data_midnight(self, mock_update):
        test_time = datetime(2020, 11, 7)
        self.assertEqual(
            self.dwd_weather.get_forecast_data(
                WeatherDataType.PRECIPITATION, test_time
            ),
            7.65,
        )

    @patch("simple_dwd_weatherforecast.dwdforecast.Weather.update", return_value=None)
    def test_get_forecast_data_after_midnight_short(self, mock_update):
        test_time = datetime(2020, 11, 7, 0, 43)
        self.assertEqual(
            self.dwd_weather.get_forecast_data(
                WeatherDataType.PRECIPITATION, test_time
            ),
            7.65,
        )

    @patch("simple_dwd_weatherforecast.dwdforecast.Weather.update", return_value=None)
    def test_get_forecast_data_after_midnight_longer(self, mock_update):
        test_time = datetime(2020, 11, 7, 1, 43)
        self.assertEqual(
            self.dwd_weather.get_forecast_data(
                WeatherDataType.PRECIPITATION, test_time
            ),
            6.54,
        )

    @patch("simple_dwd_weatherforecast.dwdforecast.Weather.update", return_value=None)
    def test_get_forecast_data_hour_on(self, mock_update):
        test_time = datetime(2020, 11, 6, 4, 0)
        self.assertEqual(
            self.dwd_weather.get_forecast_data(
                WeatherDataType.PRECIPITATION, test_time
            ),
            0.01,
        )
