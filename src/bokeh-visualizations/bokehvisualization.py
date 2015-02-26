__author__ = 'winterflower'

# A visualization test for the simulation using Bokeh and Pandas

from bokeh.plotting import *
import numpy as np
import pandas as pd
import stationparser


def stationlocationparser(fileobject):
    station_name=[]
    station_long=[]
    station_lat=[]
    for line in fileobject:
        if line[0]!="#":
            line_elements=line.split(",")
            station_name.append(line_elements[3])
            station_long.append(float(line_elements[2]))
            station_lat.append(float(line_elements[1]))
    return station_name,station_long, station_lat


tubefile=open("geographic.txt", 'r')
parsed_tuple=stationlocationparser(tubefile)


output_file("londontube.html", title="London tube example HTML")

TOOLS="pan,wheel_zoom,box_zoom,reset,hover,save"

p = figure(title="The London Underground", tools=TOOLS)

p.circle(-0.1331, 51, size=9, color='red')

p.circle(parsed_tuple[1],parsed_tuple[2], color='red', fill_alpha=0.2, size=10, )

show(p)
