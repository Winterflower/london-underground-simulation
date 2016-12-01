"""
Commuter
"""

import time
import numpy as np
from map import Map
from graph_tool.topology import *

class Commuter:
  def __init__(self, source_station_object, destination_station_object, map):
      self.source=source_station_object
      self.destination=destination_station_object
      self.map=map
      self.create_shortest_path()
      #potential race condition and might break in the future
      self.current_station=self.shortest_path_vertex_list.pop()
      self.destination_reached=False
  def create_shortest_path(self):
    station_name_index=self.map.station_name_index
    source_vertex=station_name_index[self.source.name]
    target_vertex=station_name_index[self.destination.name]
    self.shortest_path_vertex_list_list=shortest_path(map.graph_object,source_vertex, target_vertex)
    self.shortest_path_vertex_list.reverse()
  def travel_to_next_station(self):
      if len(self.shortest_path_vertex_list)==0:
        self.destination_reached=True
      else:
        #first tell the station object you are leaving
        old_station_object=self.map.station_property_map[self.current_station_vertex]
        old_station_object.leave()
        self.current_station_vertex=self.shortest_path_vertex_list.pop()
        current_station_object=self.map.station_property_map[self.current_station_vertex]
        current_station_object.register()

     
