import unittest
from simple_dwd_weatherforecast import dwdforecast


class StationTestCase(unittest.TestCase):
    def test_get_region(self):
        self.assertEqual(
            dwdforecast.get_region("EW024"),
            "NI",
            "Wrong region",
        )
        self.assertEqual(
            dwdforecast.get_region("N4333"),
            "HE",
            "Wrong region",
        )

    def test_get_region_not_valid(self):
        self.assertIsNone(dwdforecast.get_region("10"))

    def test_region_not_in_germany(self):
        self.assertIsNone(dwdforecast.get_region("06240"))