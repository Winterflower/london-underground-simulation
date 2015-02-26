__author__ = 'winterflower'
#making an interactive plot using bokeh server

from bokeh.plotting import *
import numpy.random as np
import time

output_server("bokeh_animation")

#create the figure
circle_x=np.random_sample(10)
circle_y=np.random_sample(10)
size=np.random_sample(10)*10
random_circles=figure(title="Random Circles")
random_circles.circle(circle_x, circle_y, size=size, name="circles")

show(random_circles)

renderer = random_circles.select(dict(name="circles"))
ds = renderer[0].data_source
print ds.data

#help(ds)


while True:
    new_circle_x=np.random_sample(10)
    new_circle_y=np.random_sample(10)
    ds.data["y"] = new_circle_x
    ds.data["x"] = new_circle_y
    cursession().store_objects(ds)
    time.sleep(0.10)

