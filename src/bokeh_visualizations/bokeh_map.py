__author__ = 'winterflower'

from bokeh.plotting import figure, output_file, show, output_server, cursession, output_notebook
from bokeh.models import ColumnDataSource
import time
import sys
import numpy as np
from src import parsedata
from src import simulation_utils
sys.path.append("/home/winterflower/programming_projects/python-londontube/data")




def parse_input_file(filename, cross_reference=False,target_list=None):
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
            if cross_reference:
                if line_elements[0] in target_list:
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
            else:
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

    print "Heron Quays" in station_names

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

def bokeh_zone_colour_map(data_source, notebook=False):
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
    if notebook:
        output_notebook()
    else:
        output_file("bokeh_zonecolourlondontube.html")
    TOOLS="resize,hover,save"
    zonecolour_tubemap=figure(title="London Underground locations coloured by zone", tools=TOOLS)
    zonecolour_tubemap.plot_height=1000
    zonecolour_tubemap.plot_width=1000
    zonecolour_tubemap.circle(data_source.data["longitudes"], data_source.data["latitudes"], size=10, color=data_source.data["colours"], alpha=0.8)
    show(zonecolour_tubemap)



def bokeh_animated_colours(data_source):
    """
    Creates a coloured map of London tube stations by zone where the size of the tube station changes
    according to the number of people on the station
    :param data_source:
    :return:
    """
    print "Please make sure the bokeh-server is running before you run the script"
    output_server("bokeh_tube_stations")
    TOOLS="resize,hover,save"
    animated_figure=figure(title="London Underground", tools=TOOLS)
    animated_figure.plot_height=1000
    animated_figure.plot_width=1000
    length=len(data_source.data["longitudes"])
    size=[10 for i in range(length)]
    animated_figure.circle(data_source.data["longitudes"], data_source.data["latitudes"], size=size, color=data_source.data["colours"], alpha=0.8, name="circle")
    show(animated_figure)

    #obtain the glyph renderer
    glyph_renderer=animated_figure.select((dict(name="circle")))
    print glyph_renderer
    figure_data_source=glyph_renderer[0].data_source
    while True:
        figure_data_source.data["size"]=np.random.randint(5,25,length)
        cursession().store_objects(figure_data_source)
        time.sleep(0.1)

def main(source_data_file, target_data_file):

    #Create a coloured Bokeh map

    target_map_object=simulation_utils.Map(target_data_file)
    target_map_object.initialise_map()
    target_list=target_map_object.station_name_index.keys()
    parse_input_file(source_data_file,cross_reference=False)


if __name__=="__main__":
    source_data_file="/home/winterflower/programming_projects/python-londontube/src/data/london_stations.csv"
    target_data_file="/home/winterflower/programming_projects/python-londontube/src/data/londontubes.txt"
    main(source_data_file, target_data_file)

