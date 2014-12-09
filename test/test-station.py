"""
Tests for the Station object
"""
import sys
import unittest
sys.path.append("/home/winterflower/programming_projects/python-londontube/src")
from station import Station
from edge import Edge


class TestStationObject(unittest.TestCase):
  def setUp(self):
    self.south_hampstead=Station("South Hampstead", [])
    self.regents_park=Station("Regent's Park", [])
    self.baker_street=Station("Baker Street", [self.south_hampstead, self.regents_park])
    self.random_station=Station("Random", [])
    self.another_random_station=Station("Random", [])
  def test_returnscorrectstationname(self):
    self.assertEqual("Baker Street", self.baker_street.getName())
  def test_return_nearest_stations(self):
    self.assertEqual([self.south_hampstead, self.regents_park], self.baker_street.getNearestStations())
  def test_stationsAreEqualWhenAttributesAreEqual(self):
    self.assertTrue(self.random_station == self.another_random_station)
    
if __name__=="__main__":
  unittest.main()