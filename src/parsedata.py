__author__ = 'winterflower'

from station import Station
import re
from graph_tool.all import *

def parse_file(filename):
    """
    :param filename:
    :return: list of Station objects
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
def lookupstation(listofstations, station_name):
    """

    :param listofstations:
    :param station_name:
    :return:
    Returns the station object is a station with that name exists, otherwise returns -1
    """
    found=False
    for station_object in listofstations:
        if station_object.name == listofstations:
            found=True
            return station_object
    if not found:
        return -1


