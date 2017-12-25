"""
Author: Camilla Montonen
Description: Library file that represents a Station object on the London underground
"""
import simpy
from simpy.events import Event
import numpy.random as nr
import pdb

class Station(object):
    def __init__(self, name, env):
        self.name=name
        self.commuters=[]
        self.env=env
        self.train_arrival = Event(self.env)
        self.train_leaves = Event(self.env)
    def train_arrives(self, trainobj):
            yield self.train_arrival
            print 'Station: Train arrived'
            self.board_commuters(trainobj)
    def board_commuters(self, trainobj):
        if self.commuters:
            remaining_space = min(trainobj.capacity - trainobj.space.count, len(self.commuters))
            boarding_commuters = nr.choice(self.commuters, remaining_space, replace=False)
            for commuter in boarding_commuters:
                trainobj.onboard_customer(commuter)
            print 'Station: Finished onboarding customers'
        else:
            print 'Empty station: {0}'.format(self.name)
