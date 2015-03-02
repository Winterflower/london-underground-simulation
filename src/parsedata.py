__author__ = 'winterflower'

from station import Station
import re
from graph_tool.all import *

def parse_file(filename):
    """
    :param filename:
    :return: list of Station objects which can be further manipulated to desired object
    """
    datafile=open(filename,'r')
    #a repository for all stations in the map
    stations=[]
    for line in datafile:
        if line[0]!="#":
            line_elements=re.split('\t*',line.rstrip())
            station=Station(line_elements[0].lstrip().rstrip())
            #parse the edges and turn into dict
            neighbours={}
            edge_string_elements=line_elements[1].split(',')
            for neighbour in edge_string_elements:
                target=neighbour.split('(')[0].rstrip().lstrip()
                lines=neighbour.split('(')[1].split(')')[0].split(';')
                neighbours[target]=lines
            station.add_neighbours(neighbours)
            stations.append(station)
    return stations
def lookupstationinlist(listofstations, station_name):
    """

    :param listofstations:
    :param station_name:
    :return:
    Returns the station object is a station with that name exists, otherwise returns -1Winte
    """
    found=False
    for station_object in listofstations:
        if station_object.name == station_name:
            found=True
            return station_object
    if not found:
        return -1


def createmap(list_of_station_objects):
    graphobject=Graph()
    name_index={}
    #create a property map to store stations
    station_propertymap=graphobject.new_vertex_property("object")
    #iterate through all stations:
    # 1. get the vertex descriptor and add Station object and descriptor to property map
    for station in list_of_station_objects:
        vertex=graphobject.add_vertex()
        station_propertymap[vertex]=station
        name_index[station.name]=vertex
        station.set_vertex_descriptor(vertex)
    return graphobject, station_propertymap,name_index, list_of_stations


def create_edges(graphobject, list_of_station_objects,name_index):
    #This method assumes that the graphobject has been created
    # It is a bit hacky, but it is an easy way to guarantee
    #that all vertices exist when we want to add an edge
    #iterate through the neighbours of the station and add each to the map
    edge_propertymap=graphobject.new_edge_property("string")
    for station in list_of_station_objects:
        source_name=station.name
        source_vertex=name_index[source_name]
        neighbours_dict=station.neighbours
        for neighbour_station in neighbours_dict.keys():
            #lookup the neighbouring station and add to graph
            target_name=neighbour_station #the dict contains a string
            target_vertex=name_index[target_name]
            lines=neighbours_dict[neighbour_station]
            for tubeline in lines:
                edge=graphobject.add_edge(source_vertex,target_vertex)
                edge_propertymap[edge]=tubeline
    return graphobject, edge_propertymap

############
#Some test code
##############

list_of_stations=parse_file('data/londontubes.txt')
graph, station_prop_map, name_index, list_of_stations = createmap(list_of_stations)
finalgraph, edge_props = create_edges(graph, list_of_stations,name_index)

for edge in name_index["Acton Town"].out_edges():
    print(edge)
    print edge_props[edge]
