import unittest

from simple_dwd_weatherforecast import dwdforecast


class OptionalCapabilitiesTestCase(unittest.TestCase):
    def test_supports_apparent_temperature_returns_bool(self):
        self.assertIsInstance(
            dwdforecast.Weather.supports_apparent_temperature(),
            bool,
        )

    def test_apparent_temperature_unavailable_reason_contract(self):
        reason = dwdforecast.Weather.get_apparent_temperature_unavailable_reason()
        if dwdforecast.Weather.supports_apparent_temperature():
            self.assertIsNone(reason)
        else:
            self.assertIsInstance(reason, str)
            self.assertGreater(len(reason), 0)
