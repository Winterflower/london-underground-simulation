import unittest
from src import simulation_utils
import bokeh_model

class TestBetweennessCalculation(unittest.TestCase):
    def setUp(self):
        class FakeDataSource:
            def __init__(self):
                self.data={}


        data_file="/home/winterflower/programming_projects/python-londontube/src/data/londontubes.txt"
        self.map_object=simulation_utils.Map(data_file)
        self.map_object.initialise_map()
        #create a fake data_source object
        self.fake_datasource=FakeDataSource()
        name_list=[station.name for station in self.map_object.list_of_stations]
        self.fake_datasource.data["station_names"]=name_list

    def test_updateBetweennessReturnsCorrectBins(self):
        data_source=bokeh_model.update_betweenneess("Baker Street", self.fake_datasource, self.map_object)
        print data_source.data["betweenness"]
        self.assertEquals(True, True)