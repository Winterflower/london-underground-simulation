__author__ = 'winterflower'

import station
import graph
import re
from graph_tool.all import *
from graph_tool.topology import shortest_path

def parse_graph(fileobject):
    graphoject=graph.Graph()
    temp_neighbour_repo=[]
    for line in fileobject:
        if line[0]!='#':
            line_elements=re.split('\t*',line.rstrip())
            station_name=line_elements[0].rstrip().lstrip()
            temp_neighbour_repo.append(line_elements[1])
            temp_node=graph.Node(station_name,[])
            graphoject.addnode(temp_node)
    for i in range(len(graphoject.nodes)):
        neighbour_nodes=[]
        neighbour_names=temp_neighbour_repo[i].split(',')
        for name in neighbour_names:
            name=name.split('(')[0].lstrip()
            neighbour_node=graphoject.lookupnode(name.rstrip().lstrip())
            neighbour_nodes.append(neighbour_node)
        graphoject.nodes[i].neighbours=neighbour_nodes
    return graphoject

tubelines=open('londontubes.txt', 'r')
tubemap=parse_graph(tubelines)
for node in tubemap.nodes:
    if None in node.neighbours:
        print "Contains NONE: ", node.name



def parse_graph_forvisualization(graphobject):
    graph=Graph()
    mapping={}
    for vertex in graphobject.nodes:
        node=graph.add_vertex()
        mapping[vertex.name]=node
    #create the neighbours
    for station in mapping.keys():
        newnode=mapping[station]
        oldnode=graphobject.lookupnode(station)
        for neighbour in oldnode.neighbours:
            graph.add_edge(newnode,mapping[neighbour.name])
    return graph, mapping

graph, mapping=parse_graph_forvisualization(tubemap)


print "Finding the shortest path"


vertices, edges=shortest_path(graph, mapping["Baker Street"], mapping["Aldgate"])
print vertices



#graph_draw(graph)
