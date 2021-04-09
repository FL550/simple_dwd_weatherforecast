import unittest
from simple_dwd_weatherforecast import dwdforecast


class StationTestCase(unittest.TestCase):
    def test_get_region(self):
        self.assertEqual(
            dwdforecast.get_region("EW024"),
            "Niedersachsen",
            "Wrong region",
        )
        self.assertEqual(
            dwdforecast.get_region("N4333"),
            "Hessen",
            "Wrong region",
        )

    def test_get_region_empty(self):
        self.assertIsNone(dwdforecast.get_region("10015"))

    def test_get_region_not_valid(self):
        self.assertIsNone(dwdforecast.get_region("10"))