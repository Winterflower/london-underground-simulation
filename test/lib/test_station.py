import unittest2
from src.lib.station import Station
import simpy

class TestStation(unittest2.TestCase):
    def test_station_object_initialises(self):
        name = 'Marylebone'
        env =  simpy.Environment()
        self.station = Station(name, env)
        self.assertEquals(self.station.name, name)
