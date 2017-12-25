"""
Author: Camilla Montonen
Description: Library file that represents a commuter on the London Underground
"""
from simpy.events import Event
from simpy.resources.resource import Release

class Commuter(object):
    def __init__(self, id_number, source_station_object, destination_station_object, simpy_env_object):
        self.id_number = id_number
        self.source = source_station_object
        self.destination = destination_station_object
        self.env = simpy_env_object
        self.source.commuters.append(self)
        self.train_arrived=Event(self.env)

    def arrived_at_station(self, event):
        print 'Commuter %s: Train has arrived at destination' % self.id_number
        self.env.process(self.leave_train(event))

    def leave_train(self,event):
        yield Release(event.value.space, self.request )
        print 'Commuter %s: Has left train.' % self.id_number
        self.train_arrived=Event(self.env) #for multistage journeys re-initialise the arrived event

    def request_train_space(self, train_object):
        """

        :param train_object: Train object
        :return:
        """
        yield self.train_arrived
        self.train_space = train_object.space
        request = train_object.space.request()
        self.request = request #storing the request object on the class so we can release it later
        print 'Commuter: Submitting request for space'
        yield request
        print 'Commuter: Received space on train'
