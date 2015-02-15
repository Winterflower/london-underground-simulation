__author__ = 'winterflower'
import parsedata
import unittest

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
        neighbours=self.stations[0].neigbours
        self.assertDictEqual(neighbours, {"Chiswick Park":["District"],
                                          "South Ealing":["Picadilly"],
                                           "Turnham Green":["Picadilly"],
                                          "Ealing Common":["District", "Picadilly"]})

class TestGraphGeneration(unittest.TestCase):
    def setUp(self):
        self.testdatafile="test_data.txt"
        self.stations=parsedata.parse_file(self.testdatafile)
    def test_stationlookupreturnscorrectstation(self):
        station=parsedata.lookupstation(self.stations,"Acton Town")
        self.assertEquals(station.name, "Acton Town")
    def test_stationlookupreturnsminusoneifnotfound(self):
        station=parsedata.lookupstation(self.stations, "High Street Kensington")
        self.assertEquals(station,-1)
