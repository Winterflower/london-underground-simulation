"""
Author: Camilla Montonen
Description: Library file that represents a commuter on the London Underground
"""

class Commuter(object):
    def __init__(self, id_number, source_station_object, destination_station_object):
        self.id_number = id_number
        self.source = source_station_object
        self.destination = destination_station_object
