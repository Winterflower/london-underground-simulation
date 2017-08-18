"""
Author: Camilla Montonen
Description: Tests for train object
"""

from src.lib.train import Train
from src.lib.station import Station
from mock import MagicMock
import unittest2
import simpy

class TestTrain(unittest2.TestCase):
    def test_train_initialisation(self):
        env = simpy.Environment()
        capacity = 3
        train = Train(capacity,env)
        self.assertEquals(train.capacity, capacity)

    def test_train_process(self):
        env = simpy.Environment()
        capacity=3
        train = Train(capacity,env)
        station_list=[ Station('Marylebone', env), Station('Baker Street', env), Station('Bond Street', env) ]
        train.initialise(station_list)
        env.process(train.run())
        env.run(until=10)
