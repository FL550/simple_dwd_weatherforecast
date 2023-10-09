import random
import unittest

from simple_dwd_weatherforecast import dwdforecast
import json


class StationsFileTestCase(unittest.TestCase):
    FILE_NAME = "stations.json"

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
        self.assertTrue(self.stations["H721"]["name"] == "Bedburg-Weiler Hohen")
        self.assertTrue(self.stations["78458"]["name"] == "Puerto Plata")
        self.assertTrue(self.stations["H361"]["name"] == "Beckum-Unterberg")
