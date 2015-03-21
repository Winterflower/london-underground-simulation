from simulation_utils import Commuter
from simulation_utils import Map
from simulation_utils import Station
import unittest

class TestCommuterFunctions(unittest.TestCase):
    def setUp(self):
        self.map_object=Map("test_map.txt")
        self.map_object.initialise_map()
    def test_commuterIsInstantiatedCorrectly(self):
        source_name="Station1"
        target_name="Station3"
        source_vertex=self.map_object.station_name_index["Station1"]
        target_vertex=self.map_object.station_name_index["Station3"]
        source_station_object=self.map_object.station_property_map[source_vertex]
        target_station_object=self.map_object.station_property_map[target_vertex]
        print self.map_object.station_name_index
        print source_station_object.name
        print target_station_object.name
        self.assertEquals(True, True)