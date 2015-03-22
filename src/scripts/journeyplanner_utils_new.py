__author__ = 'winterflower'

import sys
sys.path.append('/home/winterflower/programming_projects/python-londontube/src')
print sys.path
from src import parsedata
from src import simulation_utils
from graph_tool.topology import *


def print_options():
    options={"help":"For help, please type 'help'",
            "shortest":"To find the shortest path between two Tube stations type 'shortest'",
             "exit":"To exit the planner, type 'exit'"}
    for option in options.keys():
        print options[option]

def initialise_planner():
    map=simulation_utils.Map('/home/winterflower/programming_projects/python-londontube/src/data/londontubes.txt')
    map.initialise_map()
    return map

def find_shortest_path(map, source, destination):
    vertices=shortest_path(map.graph_object, map.station_name_index[source], map.station_name_index[destination])[0]
    for vertex in vertices:
        print map.station_property_map[vertex].name


def parser(command, map):
    if command=="help":
        print "HAHA, I don't have a help functionality"
    elif command=="shortest":
        print "From: "
        source=raw_input()
        print "To: "
        destination=raw_input()
        find_shortest_path(map,source,destination)

    elif command=="exit":
        return 0
    else:
        print "Apologies, the command was not recognized"


def main():
    print "####################***#####################"
    print "##########SIMPLE JOURNEY PLANNER############"
    print "####################***#####################"

    print "Welcome to the London Underground"
    print_options()
    map=initialise_planner()


    while True:
        print "Please enter command"
        command=raw_input()
        code=parser(command,map)
        if code==0:
            break


if __name__=="__main__":
    main()
