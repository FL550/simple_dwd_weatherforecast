"""Tests for the likely 1h precipitation range (PRECIPITATION_MIN/MAX).

The range is derived from the MOSMIX_L exceedance probabilities. The live
fixture MOSMIX_L_2026111203_16120.kmz (Genua) was captured during heavy rain.
"""

import re
import unittest
from unittest.mock import MagicMock, patch

from simple_dwd_weatherforecast import dwdforecast
from simple_dwd_weatherforecast.dwdforecast import WeatherDataType

MIN_KEY = WeatherDataType.PRECIPITATION_MIN.value[0]
MAX_KEY = WeatherDataType.PRECIPITATION_MAX.value[0]

# Genua 2026-11-12T09:00Z, in PRECIPITATION_EXCEEDANCE_LADDER order.
GENUA_09Z = [81.0, 81.0, 82.0, 82.0, 80.0, 78.0, 70.0, 62.0, 51.0, 30.0, 12.0, 4.0]


class PrecipitationRangeLiveTestCase(unittest.TestCase):
    FILE_NAME = "development/MOSMIX_L_2026111203_16120.kmz"

    @patch("simple_dwd_weatherforecast.dwdforecast.httpx.get")
    def setUp(self, mock_get):
        with open(self.FILE_NAME, "rb") as kmz:
            mock_get.return_value = MagicMock(
                status_code=200, headers={"ETag": "test"}, content=kmz.read()
            )
        dwd_weather = dwdforecast.Weather("16120")
        dwd_weather.download_latest_kml("16120")
        assert dwd_weather.forecast_data is not None
        self.forecast_data = dwd_weather.forecast_data

    def test_range_during_rain(self):
        # Verifies a heavy-rain hour gives a range reaching well above 0.
        data = self.forecast_data["2026-11-12T09:00:00.000Z"]
        self.assertEqual(data[MIN_KEY], 0.0)
        self.assertEqual(data[MAX_KEY], 17.5)

    def test_max_unknown_above_ladder(self):
        # Verifies MAX is None when P(>25 mm) is still above 10 % (40 % here).
        data = self.forecast_data["2026-11-12T12:00:00.000Z"]
        self.assertEqual(data["RR1c"], 19.7)
        self.assertEqual(data[MIN_KEY], 0.0)
        self.assertIsNone(data[MAX_KEY])


class PrecipitationRangeMissingElementsTestCase(unittest.TestCase):
    def test_no_ladder_elements(self):
        # Verifies data without the ladder elements (like MOSMIX_S) gives None.
        with open("development/TEST_N4333.kml", "rb") as kml:
            content = kml.read()
        codes = "|".join(c for c, _ in dwdforecast.PRECIPITATION_EXCEEDANCE_LADDER)
        content = re.sub(
            rb'<dwd:Forecast dwd:elementName="(?:' + codes.encode() + rb')">.*?'
            rb"</dwd:Forecast>",
            b"",
            content,
            flags=re.S,
        )
        dwd_weather = dwdforecast.Weather("N4333")
        dwd_weather.parse_kml(content)
        assert dwd_weather.forecast_data is not None
        for data in dwd_weather.forecast_data.values():
            self.assertIsNone(data[MIN_KEY])
            self.assertIsNone(data[MAX_KEY])


class PrecipitationQuantileTestCase(unittest.TestCase):
    def setUp(self):
        self.dwd_weather = dwdforecast.Weather("N4333")

    def quantile(self, probabilities, quantile):
        return self.dwd_weather.get_precipitation_quantile(probabilities, quantile)

    def test_dry(self):
        # Verifies a zero-probability ladder gives 0.0 for both ends.
        self.assertEqual(self.quantile([0.0] * 12, 0.1), 0.0)
        self.assertEqual(self.quantile([0.0] * 12, 0.9), 0.0)

    def test_interpolation(self):
        # Verifies linear interpolation between the thresholds around the target.
        self.assertEqual(self.quantile(GENUA_09Z, 0.1), 0.0)
        self.assertEqual(self.quantile(GENUA_09Z, 0.9), 17.5)

    def test_min_above_zero(self):
        # Verifies MIN rises above 0 when rain is near-certain.
        probabilities = [100.0, 80.0] + [0.0] * 10
        self.assertEqual(self.quantile(probabilities, 0.1), 0.15)

    def test_non_monotone_ladder(self):
        # Verifies a non-monotone ladder equals its non-increasing correction.
        raw = [17.0, 13.0, 15.0, 16.0, 10.0, 13.0, 11.0, 5.0, 1.0, 1.0, 0.0, 0.0]
        fixed = [17.0, 13.0, 13.0, 13.0, 10.0, 10.0, 10.0, 5.0, 1.0, 1.0, 0.0, 0.0]
        self.assertEqual(self.quantile(raw, 0.9), 0.7)
        self.assertEqual(self.quantile(fixed, 0.9), 0.7)

    def test_target_exactly_at_last_threshold(self):
        # Verifies P(>25 mm) of exactly 10 % gives 25.0, not None (float target).
        probabilities = [86.0, 79.0, 84.0, 83.0, 81.0, 77.0]
        probabilities += [74.0, 65.0, 61.0, 44.0, 28.0, 10.0]
        self.assertEqual(self.quantile(probabilities, 0.9), 25.0)

    def test_above_ladder(self):
        # Verifies MAX is None when the curve never drops to 10 %.
        self.assertIsNone(self.quantile([90.0] * 11 + [40.0], 0.9))

    def test_all_missing(self):
        # Verifies a ladder without any value gives None.
        self.assertIsNone(self.quantile([None] * 12, 0.9))

    def test_missing_threshold_skipped(self):
        # Verifies a missing threshold (RR1w1) is skipped, not treated as 0.
        probabilities: list[float | None] = list(GENUA_09Z)
        probabilities[10] = None
        self.assertEqual(self.quantile(probabilities, 0.9), 21.54)

    def test_below_available_ladder(self):
        # Verifies a missing low ladder gives None, not an unsupported 0.0.
        self.assertIsNone(self.quantile([None] * 9 + [0.0] * 3, 0.9))

    def test_exact_match_single_probability(self):
        # Verifies one probability equal to the target returns its threshold.
        self.assertEqual(self.quantile([None] * 11 + [10.0], 0.9), 25.0)
