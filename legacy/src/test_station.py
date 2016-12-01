__author__ = 'winterflower'
import unittest
from simulation_utils import Station
from simulation_utils import Map
from simulation_utils import Commuter
"""
Tests for the station object
"""

class TestStationObject(unittest.TestCase):
    def setUp(self):
        #do nothing
        pass
    def test_stationinitialisezwithcorrectname(self):
        station_object=Station("Station1")
        self.assertEquals(station_object.name, "Station1")
    def test_stationinitializeswithcorrectinitialcommuternumber(self):
        station_object=Station("Station1")
        self.assertEquals(station_object.number_of_initial_commuters,0)
    def test_stationinitializeswithcorrectnumberofcurrentcommuters(self):
        station_object=Station("Station2")
        self.assertEquals(station_object.number_of_current_commuters,0)
    def test_setnumberofinitialcommuters(self):
        station_object=Station("Station1")
        station_object.set_number_of_initial_commuters(100)
        self.assertEquals(station_object.number_of_initial_commuters,100)
        self.assertEquals(station_object.number_of_current_commuters,100)


class TestStationCommuterObjectInteraction(unittest.TestCase):
    def setUp(self):
        self.map_object=Map("test_map.txt")
        self.map_object.initialise_map()
        self.test_station_vertex_Station1=self.map_object.station_name_index["Station1"]
        self.test_station_object_Station1=self.map_object.station_property_map[self.test_station_vertex_Station1]
        self.test_station_object_Station3=self.map_object.station_property_map[self.map_object.station_name_index["Station3"]]
        #initialise station with 2 commuters
        self.test_station_object_Station1.set_number_of_initial_commuters(2)
        list_of_target_station_objects=[self.test_station_object_Station3, self.test_station_object_Station3]
        self.test_station_object_Station1.create_initial_commuters(list_of_target_station_objects, self.map_object)

    def test_StationCorrectlyCreatesCommuters(self):
        current_commuters=self.test_station_object_Station1.commuters
        self.assertEquals(current_commuters[0].source.name, "Station1")
        self.assertEquals(current_commuters[1].destination.name, "Station3")
    def test_StationUpdatesCurrentCommuterNumberCorrectly(self):
        one_commuter=self.test_station_object_Station1.commuters[0]
        one_commuter.travel_to_next_station()
        self.assertEquals(self.test_station_object_Station1.number_of_current_commuters,1)
        print self.test_station_object_Station1.commuters




