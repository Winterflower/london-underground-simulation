__author__ = 'winterflower'
import unittest
from map import Map
import main

class TestMainSimulation(unittest.TestCase):
    def setUp(self):
        self.map=Map('data/londontubes.txt')
        self.map.initialise_map()
    def test_create_random_target_stations_returns_correct_number(self):
        self.target_stations=main.create_random_target_stations(self.map, 800)
        self.assertEquals(800, len(self.target_stations))

