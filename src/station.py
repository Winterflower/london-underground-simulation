"""
Represents the station object
Learned about the __eq_method from http://stackoverflow.com/questions/390250/elegant-ways-to-support-equivalence-equality-in-python-classes
"""

import numpy as np
try:
    import commuter
except:
    print "Please make sure the commuter module is imported and configured correctly"

class Station():
    def __init__(self, name):
        self.name=name
        self.number_of_commuters=0
    def add_neighbours(self, neighbours):
        self.neighbours=neighbours
    def set_number_of_commuters(self, number):
        self.number_of_commuters=number
    def create_initial_commuters(self, target_stations):
        self.commuters=[]
        for i in range(self.number_of_commuters):
            self.commuters.append(commuter.Commuter(self, target_stations[i]))
    def set_vertex_descriptor(self,vertex_descriptor):
        self.vertex_descriptor=vertex_descriptor


