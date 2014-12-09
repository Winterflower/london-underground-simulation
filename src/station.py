"""
Represents the station object
Learned about the __eq_method from http://stackoverflow.com/questions/390250/elegant-ways-to-support-equivalence-equality-in-python-classes
"""

class Station():
  def __init__(self, name, nearest_stations):
    self.name=name
    self.nearest_stations=nearest_stations
  def getName(self):
    return self.name
  def getNearestStations(self):
    return self.nearest_stations
  def __eq__(self,other):
    if isinstance(other, self.__class__):
      return self.__dict__==other.__dict__
    else:
      return False