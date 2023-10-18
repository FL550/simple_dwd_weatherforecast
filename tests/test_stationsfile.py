import random
import unittest
import json


class StationsFileTestCase(unittest.TestCase):
    FILE_NAME = "simple_dwd_weatherforecast/stations.json"

    def setUp(self):
        with open(self.FILE_NAME, encoding="utf-8", mode="r") as file:
            self.stations = json.load(file)

    def test_all_properties(self):
        random_item = random.choice(list(self.stations.items()))[1]
        self.assertTrue("icao" in random_item)
        self.assertTrue("report_available" in random_item)
        self.assertTrue("name" in random_item)
        self.assertTrue("lat" in random_item)
        self.assertTrue("lon" in random_item)
        self.assertTrue("elev" in random_item)
        self.assertTrue("bundesland" in random_item)

    def test_contains(self):
        self.assertTrue("N7651" in self.stations)
        self.assertTrue("X104" in self.stations)
        self.assertTrue("78458" in self.stations)
        self.assertTrue("48564" in self.stations)

    def test_correct_mapping(self):
        self.assertEqual(self.stations["H721"]["name"], "Bedburg-Weiler Hohen")
        self.assertEqual(self.stations["78458"]["name"], "Puerto Plata")
        self.assertEqual(self.stations["H361"]["name"], "Beckum-Unterberg")

    def test_bundesland(self):
        self.assertEqual(self.stations["10452"]["bundesland"], "NI")
        self.assertEqual(self.stations["10147"]["bundesland"], "HH")
