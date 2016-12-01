__author__ = 'winterflower'

from bokeh.plotting import *


output_file("londontube.html", title="London tube example HTML")

TOOLS="pan,wheel_zoom,box_zoom,reset,hover,save"

p = figure(title="The London Underground", tools=TOOLS)