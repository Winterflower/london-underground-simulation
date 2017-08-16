"""
Main simulation application - currently mainly used for testing code functionality
"""
import sys
sys.path.append("/home/camilla/development/python/london-underground-simulation/")
from src.lib.station import Station
from src.lib.train import Train
from src.lib.commuter import Commuter
from src.monitoring.monitor_utils import patch_resource
from data.tubelines import TUBELINES
import simpy
from simpy.core import Environment
import random
from collections import defaultdict, OrderedDict
import argparse

def convert_to_station_obj(station_strings, env):
    ''' Convert list of station strings to station objs'''
    result = [ (name, Station(name, env)) for name in station_strings]
    o_dict = OrderedDict(result)
    return o_dict

def initialise_commuters(n, stationsdict, env):
    '''Initialises a random number of commuters'''
    station_list = stationsdict.values()
    result = []
    commuter_list = defaultdict(int)
    for i in range(n):
        source = random.choice(station_list)
        dest = random.choice(station_list[min(station_list.index(source)+1, len(station_list)-1):])
        commuter = Commuter(i, source, dest, env ) 
        result.append(commuter)
        commuter_list[source.name]+=1
    return result, commuter_list

def main(commuters=10, sim_max_time=700, train_capacity=800):
    env = Environment()
    data=[]
    train = Train(train_capacity, env)
    train.start_monitor(data)
    station_objs = convert_to_station_obj(TUBELINES['Jubilee'], env)
    train.set_stations(station_objs.values())
    commuters, stats = initialise_commuters( commuters, station_objs, env )
    train._initialise_arrival_events()
    env.process(train.run())
    for station in station_objs.itervalues():
        env.process(station.train_arrives(train))
    for commuter in commuters:
        env.process(commuter.request_train_space(train))
    env.run(until=sim_max_time)
    print '****DATA*****', data

def create_parser():
    parser = argparse.ArgumentParser(description='Simulate a Jubilee Line journey.')
    parser.add_argument('commuters', type=int, nargs='?') 
    return parser

if __name__=='__main__':
    parser = create_parser()
    args = parser.parse_args()
    print 'Initialised Jubilee line simulation with %s commuters' % args.commuters
    main(commuters=args.commuters)
    
