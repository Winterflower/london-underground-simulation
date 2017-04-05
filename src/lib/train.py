"""
Author: Camilla Montonen
Description: Train object
"""
import simpy
from src.monitoring.monitor_utils import patch_resource
from functools import partial

def monitor_train(datalist, space):
    datapoint=(space._env.now,
               space.count,
               len(space.queue))
    datalist.append(datapoint)

class Train(object):
    def __init__(self, capacity, simpy_env):
        self.env = simpy_env
        self.capacity = capacity
        self.space = simpy.Resource( self.env, capacity=self.capacity)
        self.arrival_events={}
        self.enable_monitor=True
        
    def _initialise_arrival_events(self):
        for station in self.stations:
            self.arrival_events[station.name]=simpy.events.Event(self.env) #create an event with callbacks

    def set_stations(self,station_list):
        self.stations=station_list

    def start_monitor(self, data):
        if self.enable_monitor:
            print 'Initialising monitor func'
            self.monitor_func = partial(monitor_train, data)
            patch_resource(self.space, post=self.monitor_func)

    def onboard_customer(self, customer):
        '''Checks the customers destination and register it as a callback in arrival events'''
        customer.train_arrived.succeed()
        event = self.arrival_events[customer.destination.name]
        event.callbacks.append(customer.arrived_at_station)
        print 'Train: Successfully registered customer %s with destination %s' %(customer.id_number, customer.destination.name)

    def run(self):
        for station in self.stations:
            print 'Train: Driving to next station'
            print station.name
            arrival_event = self.env.timeout(2)
            yield arrival_event
            print 'Train: Arrived at the next station'
            ev = self.arrival_events[station.name]
            print ev.callbacks
            ev.succeed(value=self) #send the train object back to the customer
            station.train_arrival.succeed() 
            print 'Train: Current capacity at %s' % self.space.count
            
            




"""
When train arrives at station trigger the arrival even for that station, 
each commuter should store a reference to this even
"""
