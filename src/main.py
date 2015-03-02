__author__ = 'winterflower'

"""
This is the main control center of the simulation
"""
import time
import numpy as np
from map import Map
from graph_tool.topology import *

##########################
#Initial objects needed
##########################
print "Creating Tube Map"
map=Map('data/londontubes.txt')
map.initialise_map()

def create_random_target_stations(map, number_of_commuters):
    """
    Creates a random list of target stations for commuter objects to use
    :param map:
    :return list of target stations:
    """
    target_stations=[]
    for i in range(number_of_commuters):
        #-1, because the low and high are inclusive in np.random.random_integers
        vertex=map.graph_object.vertex(np.random.random_integers(0,map.graph_object.num_vertices()-1))
        station=map.station_property_map[vertex]
        target_stations.append(station)
    return target_stations

def initialise_commuters(map, list_of_targets):
    for vertex in map.graph_object.vertices():
        initial_commuter_number=np.random.random_integers(1,4000)
        station_object=map.station_property_map[vertex]
        station_object.set_number_of_commuters=initial_commuter_number
        station_object.create_commuter_objects(list_of_targets)


def simulate_one_cycle(map):
    #each commuter calculates the shortest distance to his target
    for vertex in map.graph_object.vertices():
        station=map.station_property_map[vertex]
        for commuter in station.commuters:
            shortest_path_vertices=shortest_path(commuter.source.vertex_descriptor, commuter.targer.vertex_descriptor)


