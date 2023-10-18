import unittest
from simple_dwd_weatherforecast import dwdforecast


class LocationToolsTestCase(unittest.TestCase):
    def test_get_nearest_station_id(self):
        self.assertEqual(
            dwdforecast.get_nearest_station_id(50.291472, 8.607336),
            "L732",
            "Wrong nearest station",
        )
        self.assertEqual(
            dwdforecast.get_nearest_station_id(50.357, 8.751),
            "L635",
            "Wrong nearest station",
        )
        self.assertEqual(
            dwdforecast.get_nearest_station_id(51.290303, 6.763528),
            "10400",
            "Wrong nearest station",
        )

    def test_stations_ordered_by_distance(self):
        list = dwdforecast.get_stations_sorted_by_distance(51.291472, 8.607336)
        self.assertGreater(
            list[1][1],
            list[0][1],
            "List not ordered by distance",
        )

    def test_distance_in_km(self):
        self.assertEqual(
            dwdforecast.get_distance(49.9917, 8.41321, 50.0049, 8.42182), 1.6
        )
        self.assertEqual(
            dwdforecast.get_distance(52.5164, 13.3777, 38.69266, -9.177944), 2335.1
        )
