"""
Edge Object
Represents the Tube line connecting the two stations together
"""
class Edge():
  def __init__(self, firstVertex, secondVertex, tubeLine):
    self.firstVertex = firstVertex
    self.secondVertex = secondVertex
    self.tubeLine = tubeLine
  
  