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
    zones=[]
    zone_colour_map={ "1":"#a6cee3",
                      "2":"#1f78b4",
                      "3":"#b2df8a",
                      "4":"#33a02c",
                      "5":"#fb9a99",
                      "6":"#e31a1c",
                      "7":"#fdbf6f",
                      "8":"#ff7f00",
                      "9":"#cab2d6",
                      "mixed":"#984ea3",
                      "empty":"#020101"
    }
    for line in file_object:
        if line[0]!="%":
            line_elements=line.split(',')
            if len(line_elements)<8:
                latitudes.append(float(line_elements[3]))
                longitudes.append(float(line_elements[4]))
                station_names.append(line_elements[0])
                zone=line_elements[5].lstrip('\"').rstrip('\"')
                if zone==' ' or zone=='':
                    zones.append("empty")
                else:
                    zones.append(line_elements[5].lstrip('\"').rstrip('\"'))
            else:
                latitudes.append(float(line_elements[3]))
                longitudes.append(float(line_elements[4]))
                station_names.append(line_elements[0])
                zones.append("mixed")
    print zones

    column_data_source=ColumnDataSource(data=dict(station_names=station_names,
                                                  latitudes=latitudes,
                                                  longitudes=longitudes,
                                                  colours=[zone_colour_map[x] for x in zones]))
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
    tubemap.circle(data_source.data["longitudes"], data_source.data["latitudes"], size=5, color="blue")
    show(tubemap)

def bokeh_zone_colour_map(data_source):
    """
    Colour each station depending on the zone
    :param data_source:
    :return:
    """
    """
    :param data_source:
    :return:
    """
    #define the colours for each zone
    output_file("bokeh_zonecolourlondontube.html")
    TOOLS="resize,hover,save"
    zonecolour_tubemap=figure(title="London Underground locations coloured by zone", tools=TOOLS)
    zonecolour_tubemap.plot_height=1000
    zonecolour_tubemap.plot_width=1000
    zonecolour_tubemap.circle(data_source.data["longitudes"], data_source.data["latitudes"], size=10, color=data_source.data["colours"], alpha=0.8)
    show(zonecolour_tubemap)



data_file="/home/winterflower/programming_projects/python-londontube/src/data/london_stations.csv"
bokeh_main_map(parse_input_file(data_file))
bokeh_zone_colour_map(parse_input_file(data_file))

