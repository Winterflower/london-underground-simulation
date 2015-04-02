"""
Edge Object
Represents the Tube line connecting the two stations together
"""
class Edge():
  def __init__(self, source, target, line):
    self.source=source
    self.target=target
    self.line=line
