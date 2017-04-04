import unittest2
from src.lib.station import Station

class TestStation(unittest2.TestCase):
    def test_station_object_initialises(self):
        name = 'Marylebone'
        self.station = Station(name)
        self.assertEquals(self.station.name, name)
        
