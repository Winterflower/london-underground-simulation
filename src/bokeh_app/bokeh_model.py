from graph_tool.centrality import betweenness
from src import  simulation_utils
import numpy as np
import math
from src.bokeh_visualizations import bokeh_map

"""
Backend functions for computing visualization logic
"""
geo_file="/home/winterflower/programming_projects/python-londontube/src/data/london_stations.csv"
data_file="/home/winterflower/programming_projects/python-londontube/src/data/londontubes.txt"
map=simulation_utils.Map(data_file)
map.initialise_map()
original_data_source=bokeh_map.parse_input_file(geo_file, cross_reference=True, target_list=map.station_name_index.keys())


def filter_by_station_name(name_string, map_object, original_data_source):
    """
    Computes betweenness for all stations in the datasource
    :param data_source:
    :return:
    """
    #unset a previous vertex filter

    #create vertex filtering property map
    filterer_property_map=map_object.graph_object.new_vertex_property("boolean")
    #populate the filterer
    for vertex in map_object.graph_object.vertices():
        if map_object.station_property_map[vertex].name==name_string:
            filterer_property_map[vertex]=False
        else:
            filterer_property_map[vertex]=True
    map_object.graph_object.set_vertex_filter(filterer_property_map)
    return map_object

def calculate_betweenness(map_object, original_data_source, filtered_name_string):
    betweenness_property_map=betweenness(map_object.graph_object)[0]
    betweennes_list=[]
    for station_name_string in original_data_source.data["station_names"]:
        if station_name_string==filtered_name_string:
            betweennes_list.append(-1)
        else:
            vertex=map_object.station_name_index[station_name_string]
            betweennes_list.append(betweenness_property_map[vertex])
    return betweennes_list

def update_betweenneess(filtered_station_name):
    """
    The method that is called from the view
    :param filtered_station_name:
    :return:
    """
    filtered_map_object=filter_by_station_name(filtered_station_name, map,original_data_source)
    new_betwenneess=calculate_betweenness(filtered_map_object, original_data_source,filtered_station_name)
    #parse betweenness into buckets
    max_betwenness=max(new_betwenneess)
    betweenness_bin_list=np.digitize(new_betwenneess,np.linspace(0,max_betwenness,num=5), right=True)
    betweenness_color_map={ "0":"#ca0020",
                      "1":"#f4a582",
                      "2":"#ffffff",
                      "3":"#bababa",
                      "4":"#404040"
    }
    #add betweenness to data_source
    original_data_source.data["betweenness"]=new_betwenneess
    original_data_source.data["colours"]=[betweenness_color_map[str(x)] for x in betweenness_bin_list]
    return original_data_source


