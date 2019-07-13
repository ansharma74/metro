

'''
Filename: geopy_india_metros_culture.py
Info: Anil Sharma (sharma_anil@yahoo.com); CBIR

Draw -10 Main culture zones- & -20 Metro cities- locations on a map of India.
Mark Metro Score

Input data:
    Map-files: map_files/gadm36_IND_1
               map_files/gadm36_IND_1
               map_files/gadm36_IND_1
    Input location info. file: datafiles/City_Metro_data.csv
    Input location info. file: datafiles/Metro_Culture.csv

Usage example:
     ./geopy_india_metros_culture.py

Output:
     Output map-gif file: output/ind_10_zones_20_metros.png

'''

# Draw the locations of cities on a map of the US

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap as Basemap
from geopy.geocoders import Nominatim
from matplotlib.patches import Polygon
from matplotlib.colors import rgb2hex
import matplotlib.lines as mlines
import math
import pprint
import csv
import geopy
import pandas as pnds
from colored import fg

geopy.geocoders.options.default_timeout = None
#City Database file
city_file = "datafiles/top200engg.csv"
zone_file = "datafiles/Metro_Culture.csv"

zones = {}
zones = csv.DictReader(open(zone_file, 'r'))

cities = {}
cities = csv.DictReader(open(city_file, 'r'))

scale = 2
c_border = '#a4e6f9'

map = Basemap(llcrnrlon=69,llcrnrlat=6,urcrnrlon=100,urcrnrlat=35,projection='lcc', lon_0 = 77, lat_0 = 22)
# load the shapefile, use the name 'states'
map.readshapefile('map_files/gadm36_IND_1', name='states', drawbounds=True, color = c_border)
map.drawcountries(color = c_border)
map.drawcoastlines(color = c_border)

colors={}
zone_info={}
state_zone_info={}
cmap = plt.cm.rainbow # use 'hot' colormap
vmin = 0; vmax = 500 # set range.

# collect the state names from the shapefile attributes so we can
# look up the shape obect for a state by it's name
state_names = []
metro_cities = {"Bengaluru" : 1, "Chennai" : 1, "Bhubaneswar" : 1, "Nagpur" : 1, "Mumbai" : 1, "Jaipur" : 1,
                 "Lucknow" : 1, "Guwahati" : 1, "Jammu" : 1, "Delhi" : 1}

for rows in zones:
    state_zone_info[rows["State"]] = rows["Culture"]
    if rows["Culture"] not in zone_info:
        zone_info[rows["Culture"]] = {}

    if rows["State"] not in zone_info[rows["Culture"]]:
        zone_info[rows["Culture"]][rows["State"]] = {}
        zone_info[rows["Culture"]][rows["State"]]['Metro'] = rows["Metro"]
        zone_info[rows["Culture"]][rows["State"]]['GDP'] = rows["GDP"]
        zone_info[rows["Culture"]][rows["State"]]['Area'] = rows["Area"]
        zone_info[rows["Culture"]][rows["State"]]['Population'] = rows["Population"]
        zone_info[rows["Culture"]][rows["State"]]['Hindu'] = rows["Hindu"]
        zone_info[rows["Culture"]][rows["State"]]['Muslim'] = rows["Muslim"]
        zone_info[rows["Culture"]][rows["State"]]['Christan'] = rows["Christan"]
        zone_info[rows["Culture"]][rows["State"]]['Sikh'] = rows["Sikh"]
    else:
        zone_info[rows["Culture"]][rows["State"]]['Metro'] = rows["Metro"]
        zone_info[rows["Culture"]][rows["State"]]['GDP'] = rows["GDP"]
        zone_info[rows["Culture"]][rows["State"]]['Area'] = rows["Area"]
        zone_info[rows["Culture"]][rows["State"]]['Population'] = rows["Population"]
        zone_info[rows["Culture"]][rows["State"]]['Hindu'] = rows["Hindu"]
        zone_info[rows["Culture"]][rows["State"]]['Muslim'] = rows["Muslim"]
        zone_info[rows["Culture"]][rows["State"]]['Christan'] = rows["Christan"]
        zone_info[rows["Culture"]][rows["State"]]['Sikh'] = rows["Sikh"]

pprint.pprint(zone_info, width=1)

for shape_dict in map.states_info:
    state_names.append(shape_dict['NAME_1'])
    # get states and choose color based on zone
    state_culture = state_zone_info[shape_dict['NAME_1']]
    if state_culture == 'A':
        pop = 10
        colors[shape_dict['NAME_1']] = cmap(1-np.sqrt((pop-vmin)/(vmax-vmin)))[:3]
        continue
    if state_culture == 'B':
        pop = 70
        colors[shape_dict['NAME_1']] = cmap(1-np.sqrt((pop-vmin)/(vmax-vmin)))[:3]
        continue
    if state_culture == 'C':
        pop = 35
        colors[shape_dict['NAME_1']] = cmap(1-np.sqrt((pop-vmin)/(vmax-vmin)))[:3]
        continue
    if state_culture == 'H':
        pop = 110 
        colors[shape_dict['NAME_1']] = cmap(1-np.sqrt((pop-vmin)/(vmax-vmin)))[:3]
        continue
    if state_culture == 'K':
        pop = 137
        colors[shape_dict['NAME_1']] = cmap(1-np.sqrt((pop-vmin)/(vmax-vmin)))[:3]
        continue
    if state_culture == 'M':
        pop = 210
        colors[shape_dict['NAME_1']] = cmap(1-np.sqrt((pop-vmin)/(vmax-vmin)))[:3]
        continue
    if state_culture == 'P':
        pop = 260
        colors[shape_dict['NAME_1']] = cmap(1-np.sqrt((pop-vmin)/(vmax-vmin)))[:3]
        continue
    if state_culture == 'T':
        pop = 22 
        colors[shape_dict['NAME_1']] = cmap(1-np.sqrt((pop-vmin)/(vmax-vmin)))[:3]
        continue
    if state_culture == 'U':
        pop = 200 
        colors[shape_dict['NAME_1']] = cmap(1-np.sqrt((pop-vmin)/(vmax-vmin)))[:3]
        continue
    if state_culture == 'W':
        pop = 300
        colors[shape_dict['NAME_1']] = cmap(1-np.sqrt((pop-vmin)/(vmax-vmin)))[:3]
        continue

ax = plt.gca() # get current axes instance
for nshape,seg in enumerate(map.states):
    l_facecolor = rgb2hex(colors[state_names[nshape]])
    poly = Polygon(seg,facecolor=l_facecolor,edgecolor = c_border) # a dull orange
    ax.add_patch(poly)

print("########## Done plotting zones ###############")

# Get the location of each city and plot it
geolocator = Nominatim()
for rows in cities:
    l_city = rows["Main City"]
    loc = geolocator.geocode(l_city)
    x, y = map(loc.longitude, loc.latitude)
    map.plot(x,y,marker='*',color='#00acdb',markersize=scale, markeredgecolor="m")
    print(fg('orchid') + "MAP: Cities:",rows["Rank"],l_city)
    
    if l_city == 'Bengaluru' and metro_cities["Bengaluru"] == 1 :
        plt.text(x, y, "  " + l_city + "( -" + "- ) * Spiceland", 
                  fontweight=1000,ha='right', va='top', fontsize=4, color='black');
        metro_cities["Bengaluru"] = 0
        print("Marked Bengaluru")
    elif l_city == 'Chennai' and metro_cities["Chennai"] == 1:
        plt.text(x, y, "  " + l_city + "( -" + "- ) * Spicer-land", 
                  fontweight=1000,ha='left', va='top', fontsize=4, color='black');
        metro_cities["Chennai"] = 0
        print("Marked Chennai")
    elif l_city == 'Bhubaneswar' and metro_cities["Bhubaneswar"] == 1:
        plt.text(x, y, "  " + l_city + "( -" + "- ) * Royal Bengal", 
                  fontweight=1000,ha='left', va='top', fontsize=4, color='black');
        metro_cities["Bhubaneswar"] = 0 
        print("Marked Bhubaneswar")
    elif l_city == 'Nagpur' and metro_cities["Nagpur"] == 1:
        plt.text(x, y, "  " + l_city + "( -" + "- ) * Eastern", 
                  fontweight=1000,ha='left', va='bottom', fontsize=4, color='black');
        metro_cities["Nagpur"] = 0
        print("Marked Nagpur")
    elif l_city == 'Mumbai' and metro_cities["Mumbai"] == 1:
        plt.text(x, y, "  " + l_city + "( -" + "- ) * West Coast", 
                  fontweight=1000,ha='center', va='top', fontsize=4, color='black');
        metro_cities["Mumbai"] = 0
        print("Marked Mumbai")
    elif l_city == 'Jaipur' and metro_cities["Jaipur"] == 1:
        plt.text(x, y, "  " + l_city + "( -" + "- ) * Central", 
                  fontweight=1000,ha='right', va='top', fontsize=4, color='black');
        metro_cities["Jaipur"] = 0
        print("Marked Jaipur")
    elif l_city == 'Lucknow' and metro_cities["Lucknow"] == 1:
        plt.text(x, y, "  " + l_city + "( -" + "- ) * Hindibelt", 
                  fontweight=1000,ha='center', va='top', fontsize=4, color='black');
        metro_cities["Lucknow"] = 0
        print("Marked Lucknow")
    elif l_city == 'Guwahati' and metro_cities["Guwahati"] == 1:
        plt.text(x, y, "  " + l_city + "( -" + "- ) * Northeast", 
                  fontweight=1000,ha='center', va='top', fontsize=4, color='black');
        metro_cities["Guwahati"] = 0
        print("Marked Guwahati")
    elif l_city == 'Jammu' and metro_cities["Jammu"] == 1:
        plt.text(x, y, "  " + l_city + "( -" + "- ) * Himalyas", 
                  fontweight=1000,ha='right', va='top', fontsize=4, color='black');
        metro_cities["Jammu"] = 0
        print("Marked Jammu")
    elif l_city == 'Delhi' and metro_cities["Delhi"] == 1:
        plt.text(x, y, "  " + l_city + "( -" + "- ) * Colorful Punjab", 
                  fontweight=1000,ha='left', va='top', fontsize=4, color='black');
        metro_cities["Delhi"] = 0
        print("Marked Delhi")

print("########## Done plotting cities ###############")
print("########## Legends #####################")
cream_square = mlines.Line2D([], [], color='#cfe2d4', marker='s', linestyle='None',
                          markersize=5, label='State-Zones (Colored areas) ')
cyan_star = mlines.Line2D([], [], color='cyan', marker='*', linestyle='None',
                          markersize=5, label='Engg College Towns')
legend1 = plt.legend(handles=[cream_square, cyan_star], title='Top 200 Enguneering Colleges',
           loc='upper right' , facecolor = 'skyblue', fontsize=5)

legend1.get_title().set_fontsize('6')
plt.title('India: Top Engineering Colleges', size = 7)

plt.savefig('output/ind_top200.png', dpi=1200)

plt.show()
