__author__ = 'winterflower'

from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
import sys
sys.path.append("/home/winterflower/programming_projects/python-londontube/data")

def parse_input_file(filename):
    """
    Assumes that the file is of the form

    %Station,OS X,OS Y,Latitude,Longitude,Zone,Postcode
    Abbey Road,539081,183352,51.531951985733,0.0037377856069111,"3",E15 3NB
    :param filename:
    :return:
    """
    file_object=open(filename, 'r')
    station_names=[]
    longitudes=[]
    latitudes=[]
    for line in file_object:
        if line[0]!="%":
            line_elements=line.split(',')
            latitudes.append(float(line_elements[3]))
            longitudes.append(float(line_elements[4]))
            station_names.append(line_elements[0])

    column_data_source=ColumnDataSource(data=dict(station_names=station_names,
                                                  latitudes=latitudes,
                                                  longitudes=longitudes))
    return column_data_source


#############

def bokeh_main_map(data_source):
    #define the outputfile
    output_file("bokeh_londontube.html")
    #define tools
    TOOLS='resize,hover,save'
    tubemap=figure(title="London Underground locations", tools=TOOLS)
    tubemap.plot_height=1000
    tubemap.plot_width=1000
    tubemap.circle(data_source.data["longitudes"], data_source.data["latitudes"], size=5)
    show(tubemap)

def bokeh_line_map():
    ""

data_file="/home/winterflower/programming_projects/python-londontube/src/data/london_stations.csv"
bokeh_main_map(parse_input_file(data_file))

