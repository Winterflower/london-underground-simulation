__author__ = 'winterflower'

from graph_tool.topology import *

class Commuter:
  def __init__(self, source_station_object, destination_station_object, map):
      self.source=source_station_object
      self.destination=destination_station_object
      self.map=map
      self.shortest_path=self.create_shortest_path()
      print self.shortest_path
      #potential race condition and might break in the future
      self.current_station=self.shortest_path.pop()
      #print self.current_station
      self.destination_reached=False
  def create_shortest_path(self):
      station_name_index=self.map.station_name_index
      source_vertex=station_name_index[self.source.name]
      target_vertex=station_name_index[self.destination.name]
      #print "Checking the map"
      self.shortest_path_edge_list=shortest_path(self.map.graph_object,source_vertex, target_vertex)
      list=[]
      for element in self.shortest_path_edge_list:
          list=[element]+list
      return list
    #print type(self.shortest_path_vertex_list)
    #self.shortest_path_vertex_list.reverse()
  def travel_to_next_station(self):
      if len(self.shortest_path)==0:
        self.destination_reached=True
      else:
        #first tell the station object you are leaving
        old_station_object=self.map.station_property_map[self.current_station]
        old_station_object.leave()
        self.current_station=self.shortest_path.pop()
        current_station_object=self.map.station_property_map[self.current_station]
        current_station_object.register()




class Station:
    def __init__(self, name):
        self.name=name
        self.number_of_initial_commuters=0
        self.number_of_current_commuters=0
    def add_neighbours(self, neighbours):
        self.neighbours=neighbours
    def set_number_of_initial_commuters(self, number):
        self.number_of_initial_commuters=number
        self.number_of_current_commuters=number
    def create_initial_commuters(self, target_stations, map):
        self.commuters=[]
        for i in range(self.number_of_initial_commuters):
            self.commuters.append(Commuter(self, target_stations[i],map))
    def set_vertex_descriptor(self,vertex_descriptor):
        self.vertex_descriptor=vertex_descriptor
    def register(self):
        """
        A method called by each Customer visiting the Station
        :return:
        """
        self.number_of_current_commuters=self.number_of_current_commuters+1
    def leave(self):
        self.number_of_current_commuters=self.number_of_current_commuters-1

import parsedata

class Map():
  def __init__(self, filename):
      self.datafile=filename
  def initialise_map(self):
      self.list_of_stations=parsedata.parse_file(self.datafile)
      temp_graph, self.station_property_map, self.station_name_index, self.list_of_stations=parsedata.createmap(self.list_of_stations)
      self.graph_object, self.edge_property_map=parsedata.create_edges(temp_graph, self.list_of_stations,
                                                                       self.station_name_index)

