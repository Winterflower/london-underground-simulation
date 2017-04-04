"""
Author: Camilla Montonen
Description: Library file that represents a Station object on the London underground
"""
import simpy
from simpy.events import Event

class Station(object):
    def __init__(self, name, env):
        self.name=name
        self.commuters=[]
        self.env=env
        self.train_arrival = Event(self.env)
    def train_arrives(self, trainobj):
            yield self.train_arrival
            print 'Station: Train arrived'
            self.board_commuters(trainobj)
    def board_commuters(self, trainobj):
        for commuter in self.commuters:
            trainobj.onboard_customer(commuter)
        print 'Station: Finished onboarding customers'
