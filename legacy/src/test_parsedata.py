__author__ = 'winterflower'
import parsedata
import unittest
from graph_tool.all import *

class TestParseData(unittest.TestCase):
    def setUp(self):
        self.testdatafile="test_data.txt"
    def test_parsefilegetsallelements(self):
        self.stations=parsedata.parse_file(self.testdatafile)
        self.assertEquals(len(self.stations), 4)
    def test_parsefilegetscorrectstations(self):
        self.station_names=[]
        for station_object in parsedata.parse_file("test_data.txt"):
            self.station_names.append(station_object.name)
        self.assertListEqual(self.station_names,["Acton Town", "Aldgate", "Aldgate East", "Alperton"])
    def test_parsefilegetscorrectneighbours(self):
        self.stations=parsedata.parse_file(self.testdatafile)
        #get the neighbours of "Acton Town"
        neighbours=self.stations[0].neighbours
        print "Neighbour"
        print neighbours
        self.assertDictEqual(neighbours, {"Chiswick Park":["District"],
                                          "South Ealing":["Picadilly"],
                                           "Turnham Green":["Picadilly"],
                                          "Ealing Common":["District", "Picadilly"]})

class TestGraphGeneration(unittest.TestCase):
    def setUp(self):
        self.testdatafile="test_data.txt"
        self.stations=parsedata.parse_file(self.testdatafile)
    def test_stationlookupreturnscorrectstation(self):
        station=parsedata.lookupstationinlist(self.stations,"Acton Town")
        self.assertEquals(station.name, "Acton Town")
    def test_stationlookupreturnsminusoneifnotfound(self):
        station=parsedata.lookupstationinlist(self.stations, "High Street Kensington")
        self.assertEquals(station,-1)
    def test_graphobjecthascorrectnumberofvertices(self):
        self.graph_object, self.station_propertymap = parsedata.createmap(self.stations)
        vertices=[]
        for vertex in self.graph_object.vertices():
            vertices.append(vertex)
        self.assertEquals(4, len(vertices))
    def test_propertymapmapstotherightstationobjects(self):
        #create a list of vertex names expected based on the test data
        test_vertices=["Acton Town", "Aldgate", "Aldgate East", "Alperton"]
        vertex_counter=0
        graph_object, station_propertymap = parsedata.createmap(self.stations)
        for vertex in graph_object.vertices():
            mapped_station_object=station_propertymap[vertex]
            #vertices are returned in the order they are added accroding to the docs
            #this test relies on the above property
            print mapped_station_object.name
            self.assertEquals(test_vertices[vertex_counter], mapped_station_object.name)
            vertex_counter+=1

