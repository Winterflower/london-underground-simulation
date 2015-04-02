"""
Represents the station object
Learned about the __eq_method from http://stackoverflow.com/questions/390250/elegant-ways-to-support-equivalence-equality-in-python-classes
"""

import numpy as np
import commuter


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
            self.commuters.append(commuter.Commuter(self, target_stations[i]),map)
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



hello="hello"
new_station=Station("hello")