__author__ = 'winterflower'
import re

class Graph:
    def __init__(self):
        self.nodes=[]
        self.nodenames=[]
    def addnode(self,node):
        self.nodes.append(node)
        self.nodenames.append(node.name)
    def lookupnode(self,nodename):
        for node in self.nodes:
            if node.name==nodename:
                return node
    def print_node_info(self, nodename):
        node=self.lookupnode(nodename)
        print "Node: ", node.name
        print "Neighbours: "
        for station in node.neighbours:
            print station.name

class Node:
    def __init__(self, name, neighbours):
        self.name=name
        self.neighbours=neighbours