__author__ = 'winterflower'

from bokeh.plotting import *
import bokeh
import numpy.random as np

output_file('test-tube-map.html')

start_point_x=list(np.random_sample(10))
start_point_y=list(np.random_sample(10))
end_point_x=list(np.random_sample(10))
end_point_y=list(np.random_sample(10))

first_control_point_x=[(a+b)/2 for a in start_point_x for b in end_point_x]
first_control_point_y=[(a+b)/2 for a in start_point_y for b in end_point_y]
second_control_point_x=[2*(a+b)/3 for a in start_point_x for b in start_point_x]
second_control_point_y=[2*(a+b)/3 for a in start_point_y for b in end_point_y]

bokeh_plot=figure(title="Some funky bezier curves")
bokeh_plot.bezier(start_point_x, start_point_y, end_point_x, end_point_y, first_control_point_x, first_control_point_y,
                  second_control_point_x, second_control_point_y)
#show(bokeh_plot)

def generate_bezier_control_points(start_x, start_y, end_x_, end_y):
    """
    Automatically generates four lists of bezier curve control points for bokeh bezier plotting
    :param start_x:
    :param start_y:
    :param end_x_:
    :param end_y:
    :return:
    """
    first_control_x=[(a+b)/2 for a in start_x for b in end_x_]
    first_control_y=[(a+b)/2 for a in start_y for b in end_y]
    second_control_y=[2*(a+b)/2 for a in start_x for b in start_y]






