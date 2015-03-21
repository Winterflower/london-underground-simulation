from simulation_utils import Commuter
from simulation_utils import Map
from simulation_utils import Station
import unittest

class TestCommuterFunctions(unittest.TestCase):
    def setUp(self):
        self.map_object=Map("test_map.txt")
        self.map_object.initialise_map()
        source_name="Station1"
        target_name="Station3"
        source_vertex=self.map_object.station_name_index["Station1"]
        target_vertex=self.map_object.station_name_index["Station3"]
        source_station_object=self.map_object.station_property_map[source_vertex]
        target_station_object=self.map_object.station_property_map[target_vertex]
        print self.map_object.station_name_index
        print source_station_object.name
        print target_station_object.name
        #initialize commuter
        self.commuter=Commuter(source_station_object, target_station_object, self.map_object)
    def test_commuterSourceStationIsInstantiatedCorrectly(self):
        self.assertEquals(self.commuter.source.name, "Station1")
    def test_commuterCurrentStationIsCorrect(self):
        self.assertEquals(self.commuter.current_station,self.map_object.station_name_index["Station1"] )
    def test_commuterTravelToNextStationGivesCorrectCurrentStation(self):
        self.commuter.travel_to_next_station()
        self.assertEquals(self.commuter.current_station, self.map_object.station_name_index["Station2"])
    def test_commuterTravelToNextStationDetectsEndOfJourney(self):
        #there are only two stops to the target station
        self.commuter.travel_to_next_station()
        self.commuter.travel_to_next_station()
        self.commuter.travel_to_next_station()
        self.assertTrue(self.commuter.destination_reached)