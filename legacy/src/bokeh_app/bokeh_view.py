import bokeh_model
from bokeh.plotting import figure
from bokeh.models import Plot, ColumnDataSource
from bokeh.properties import Instance
from bokeh.server.app import bokeh_app
from bokeh.server.utils.plugins import object_page
from bokeh.models.widgets import HBox, Slider, TextInput, VBoxForm


##################
#HELPER METHOD
##################



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





"""
This file demonstrates a bokeh applet, which can be viewed directly
on a bokeh-server. See the README.md file in this directory for
instructions on running.
"""




class SlidersApp(HBox):
    """An example of a browser-based, interactive plot with slider controls."""
    plot = Instance(Plot)
    extra_generated_classes = [["SlidersApp", "SlidersApp", "HBox"]]
    source = Instance(ColumnDataSource)
    text = Instance(TextInput)


    @classmethod
    def create(cls):
        """One-time creation of app's objects.

        This function is called once, and is responsible for
        creating all objects (plots, datasources, etc)
        """


        obj = cls()
        source_data_file="/home/winterflower/programming_projects/python-londontube/src/data/london_stations.csv"
        target_data_file="/home/winterflower/programming_projects/python-londontube/src/data/londontubes.txt"
        source=parse_input_file(source_data_file,cross_reference=True,target_list=target_data_file)
        print "Initial"
        print source.data["colours"]
        print source.data["longitudes"]
        obj.source = ColumnDataSource(data=dict(longitudes=source.data["longitudes"],
                                                latitudes=source.data["latitudes"],
                                                colours=source.data["colours"]),
                                      )

        obj.text = TextInput(
            title="title", name='title', value='Enter station name'
        )


        toolset = "reset,resize,save,wheel_zoom"



        # Generate a figure container
        plot = figure(title_text_font_size="12pt",
                      plot_height=800,
                      plot_width=800,
                      tools=toolset,
                      title=obj.text.value,
        )

        plot.xaxis.axis_label = 'Longitude'
        plot.yaxis.axis_label = 'Latitude'

        # Plot the line by the x,y values in the source property
        plot.circle('longitudes', 'latitudes', fill_color='colours', source=obj.source,
                  size=10,
                  alpha=0.9

        )


        obj.plot = plot
        obj.update_data()



        obj.children.append(obj.text)
        obj.children.append(obj.plot)

        return obj

    def setup_events(self):
        """Attaches the on_change event to the value property of the widget.

        The callback is set to the input_change method of this app.
        """
        super(SlidersApp, self).setup_events()
        if not self.text:
            return

        # Text box event registration
        self.text.on_change('value', self, 'input_change')


    def input_change(self, obj, attrname, old, new):
        """Executes whenever the input form changes.

        It is responsible for updating the plot, or anything else you want.

        Args:
            obj : the object that changed
            attrname : the attr that changed
            old : old value of attr
            new : new value of attr
        """
        self.update_data()
        self.plot.title = "Removed station " + self.text.value

    def update_data(self):
        """Called each time that any watched property changes.

        This updates the sin wave data with the most recent values of the
        sliders. This is stored as two numpy arrays in a dict into the app's
        data source property.
        """
        data_source=bokeh_model.update_betweenneess(self.text.value)
        self.source.data=data_source.data




# The following code adds a "/bokeh/sliders/" url to the bokeh-server. This
# URL will render this sine wave sliders app. If you don't want to serve this
# applet from a Bokeh server (for instance if you are embedding in a separate
# Flask application), then just remove this block of code.
@bokeh_app.route("/bokeh/sliders/")
@object_page("sin")
def make_sliders():
    app = SlidersApp.create()
    return app