__author__ = 'winterflower'

"""
This is the main control center of the simulation
"""
import time
import numpy as np
import simulation_utils
from graph_tool.topology import *

##########################
#Initial objects needed
##########################


def create_random_target_station_objects(map,source_station_object, number_of_commuters):
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
        while station.name==source_station_object.name:
            vertex=map.graph_object.vertex(np.random.random_integers(0,map.graph_object.num_vertices()-1))
            station=map.station_property_map[vertex]
        target_stations.append(station)
    return target_stations



def initialise_commuters(map):
    for vertex in map.graph_object.vertices():
        initial_commuter_number=np.random.random_integers(1,40)
        station_object=map.station_property_map[vertex]
        list_of_target_station_objects=create_random_target_station_objects(map, station_object,initial_commuter_number)
        print station_object.name
        station_object.set_number_of_initial_commuters(initial_commuter_number)
        station_object.create_initial_commuters(list_of_target_station_objects, map)

def simulate_one_cycle(map):
    #each commuter calculates the shortest distance to his target
    for vertex in map.graph_object.vertices():
        station=map.station_property_map[vertex]
        for commuter in station.commuters:
            commuter.travel_to_next_station()

def main():
    print "Creating Tube Map"
    map=simulation_utils.Map('data/londontubes.txt')
    map.initialise_map()
    graph_object=map.graph_object
    initialise_commuters(map)
    vertex=map.station_name_index["Aldgate"]
    station_object=map.station_property_map[vertex]
    print station_object.number_of_current_commuters
    simulate_one_cycle(map)
    vertex=map.station_name_index["Aldgate"]
    station_object=map.station_property_map[vertex]
    print station_object.number_of_current_commuters
    for vertex in map.graph_object.vertices():
        station_object=map.station_property_map[vertex]
        print station_object.name
        print station_object.number_of_current_commuters
    

#main(map)

if __name__=="__main__":
    #do nothing
    main()






