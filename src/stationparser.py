__author__ = 'winterflower'

import station
import graph
import re
import edge
from graph_tool.all import *
from graph_tool.topology import shortest_path
from bokeh.plotting import *
import numpy as np

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

def parse_graph_edges(fileobject):
    #creates edge objects to be passed to the grapher
    edges=[]
    for line in fileobject:
        if line[0]!="#":
            line_elements=re.split('\t*',line.rstrip())
            source=line_elements[0].rstrip().lstrip()
            edge_string_elements=line_elements[1].split(',')
            for station in edge_string_elements:
                target=station.split('(')[0].rstrip().lstrip()
                lines=station.split('(')[1].split(')')[0].split(';')
                print lines
                for line in lines:
                    temp_edge=edge.Edge(source,target,line)
                    edges.append(temp_edge)
    return edges

tubeedges=open('londontubes.txt', 'r')
edges=parse_graph_edges(tubeedges)


def parse_graph_forvisualization(graphobject):
    graph=Graph()
    mapping={}
    index_name_mapping={}
    for vertex in graphobject.nodes:
        node=graph.add_vertex()
        mapping[vertex.name]=node
        index_name_mapping[graph.vertex_index[node]]=vertex.name
    #create the neighbours
    for station in mapping.keys():
        newnode=mapping[station]
        oldnode=graphobject.lookupnode(station)
        #for neighbour in oldnode.neighbours:
        #    graph.add_edge(newnode,mapping[neighbour.name])
    return graph, mapping, index_name_mapping

graph, mapping, index_name=parse_graph_forvisualization(tubemap)

def add_edges(graph, list_of_edges, station_mapping):
    edge_mapping={}
    for edge in list_of_edges:
        source_string=edge.source
        source_vertex=station_mapping[source_string]
        target_string=edge.target
        target_vertex=station_mapping[target_string]
        line_string=edge.line
        tempedge=graph.add_edge(source_vertex, target_vertex)
        edge_mapping[graph.edge_index[tempedge]]=line_string
    return edge_mapping
edge_map=add_edges(graph,edges,mapping)


####################################################
#DATA ANALYSIS ON THE GRAPH
####################################################

#calculate out-degree
out_degree={}
out_degree_array=[]
for vertex in graph.vertices():
    out_degree[int(vertex)]=vertex.out_degree()
    out_degree_array.append(vertex.out_degree())
print out_degree_array







print "Finding the shortest path"
vertices, edges=shortest_path(graph, mapping["Baker Street"], mapping["Liverpool Street"])
print "Printing path"
for station in vertices:
    print index_name[graph.vertex_index[station]]
for edge in edges:
    print "Line: ", edge_map[graph.edge_index[edge]]



#################################
#BOKEH VISUALIATION
################################

def stationlocationparser(fileobject):
    station_name=[]
    station_long=[]
    station_lat=[]
    for line in fileobject:
        if line[0]!="#":
            line_elements=line.split(",")
            station_name.append(line_elements[3])
            station_long.append(float(line_elements[2]))
            station_lat.append(float(line_elements[1]))
    return station_name,station_long, station_lat


tubefile=open("geographic.txt", 'r')
parsed_tuple=stationlocationparser(tubefile)


output_file("londontubenew.html", title="London tube example HTML")

TOOLS="pan,wheel_zoom,box_zoom,reset,hover,save"

p = figure(title="The London Underground", tools=TOOLS)
palette=["#feebe2","#fbb4b9", "#f768a1","#ae017e","#7a0177"]
min_out=min(out_degree_array)
max_out=max(out_degree_array)
color_index=[int(4*(x-min_out)/(max_out-min_out)) for x in out_degree_array]
color_map=[palette[i] for i in color_index]

p.circle(parsed_tuple[1],parsed_tuple[2], color=color_map, fill_alpha=0.8, size=10, line_color="black")

show(p)




#graph_draw(graph)
