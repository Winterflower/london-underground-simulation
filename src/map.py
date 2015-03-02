"""
The Tube Map object contains:
1. Graph object
2. Vertex propertymap
3. Edge propertymap
4. list of Station objects
5. A name_index dict to facilitate looking up Vertices based on Strings
"""
try:
    import parsedata
    import commuter
except:
    print "Please make sure the parsedata and commuter modules have installed and configured correctly"



class Map():
  def __init__(self, filename):
      self.datafile=filename
  def initialise_map(self):
      self.list_of_stations=parsedata.parse_file(self.datafile)
      temp_graph, self.station_property_map, self.station_name_index, self.list_of_stations=parsedata.createmap(self.list_of_stations)
      self.graph_object, self.edge_property_map=parsedata.create_edges(temp_graph, self.list_of_stations,
                                                                       self.station_name_index)






map = Map('data/londontubes.txt')
map.initialise_map()
  