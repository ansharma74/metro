#!/usr/bin/python3
# Draw the locations of cities on a map of India based on investment worthiness

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap as Basemap
from geopy.geocoders import Nominatim
from matplotlib.patches import Polygon
from matplotlib.colors import rgb2hex
import math
import csv
from colored import fg

#City Database file
city_file = "datafiles/City_Metro_data.csv"

cities = {}
cities = csv.DictReader(open(city_file, 'r'))

#Zones database
zone_file = "datafiles/Metro_Culture.csv"

zones = {}
zones = csv.DictReader(open(zone_file, 'r'))
metro_state_info={}
for rows in zones:
    metro_state_info[rows["Metro"]] = rows["State"]

scale = 2
c_border = '#a4e6f9'

# Figure and map 1
f1 = plt.figure(1)

map1 = Basemap(llcrnrlon=69,llcrnrlat=6,urcrnrlon=100,urcrnrlat=37, \
                       projection='lcc', lon_0 = 77, lat_0 = 22)
# load the shapefile, use the name 'states'
map1.readshapefile('/home/anil/Downloads/map_files/gadm36_IND_1', name='states', \
                       drawbounds=True, color = c_border)
map1.drawcountries(color = c_border)
map1.drawcoastlines(color = c_border)

# Figure and map 2
f2 = plt.figure(2)

map2 = Basemap(llcrnrlon=69,llcrnrlat=6,urcrnrlon=100,urcrnrlat=37, \
                       projection='lcc', lon_0 = 77, lat_0 = 22)
# load the shapefile, use the name 'states'
map2.readshapefile('/home/anil/Downloads/map_files/gadm36_IND_1', name='states', \
                       drawbounds=True, color = c_border)
map2.drawcountries(color = c_border)
map2.drawcoastlines(color = c_border)

# Figure and map 3
f3 = plt.figure(3)

map3 = Basemap(llcrnrlon=69,llcrnrlat=6,urcrnrlon=100,urcrnrlat=37, \
                       projection='lcc', lon_0 = 77, lat_0 = 22)
# load the shapefile, use the name 'states'
map3.readshapefile('/home/anil/Downloads/map_files/gadm36_IND_1', name='states', \
                       drawbounds=True, color = c_border)
map3.drawcountries(color = c_border)
map3.drawcoastlines(color = c_border)

state_names = []
for shape_dict in map1.states_info:
    state_names.append(shape_dict['NAME_1'])

state_map1 = []
state_map2 = []
state_map3 = []

cmap = plt.cm.hot # use 'hot' colormap
vmin = 0; vmax = 950 # set range.
pop1 = 100
pop2 = 200
pop3 = 300
l_facecolor1 = rgb2hex(cmap(1-np.sqrt((pop1-vmin)/(vmax-vmin)))[:3])
l_facecolor2 = rgb2hex(cmap(1-np.sqrt((pop2-vmin)/(vmax-vmin)))[:3])
l_facecolor3 = rgb2hex(cmap(1-np.sqrt((pop3-vmin)/(vmax-vmin)))[:3])

geolocator = Nominatim()

for rows in cities:
    l_metro = rows["Metro Area"]
    l_city = rows["Main City"]
    l_count = int(rows["Score(12)"])
    if int(l_count) <= 6:
        plt.figure(1)
        c_state = metro_state_info[l_city]
        state_map1.append(c_state)

        # Get the location of city and plot it
        loc = geolocator.geocode(l_city)
        x, y = map1(loc.longitude, loc.latitude)
        map1.plot(x,y,marker='o',color='Red', \
                markersize=int(math.sqrt(l_count))*scale)
        if l_city == 'Bangalore':
            plt.text(x, y, "  " + l_city + "( -" + str(l_count) + "- )", \
                fontweight=1000, ha='right', va='top', fontsize=5, color='Black');
        else:
            plt.text(x, y, "  " + l_city + "( -" + str(l_count) + "- )", \
                fontweight=1000, ha='left', va='top', fontsize=5, color='Black');

        print(fg('orchid') + "MAP1: High investment focus:", \
                l_metro, l_city, l_count)
    elif 6 < int(l_count) <= 9:
        plt.figure(2)
        c_state = metro_state_info[l_city]
        state_map2.append(c_state)

        # Get the location of city and plot it
        loc = geolocator.geocode(l_city)
        x, y = map2(loc.longitude, loc.latitude)
        map2.plot(x,y,marker='o',color='Red', \
                markersize=int(math.sqrt(l_count))*scale)
        if l_city == 'Bangalore':
            plt.text(x, y, "  " + l_city + "( -" + str(l_count) + "- )", \
                fontweight=1000, ha='right', va='top', fontsize=5, color='Black');
        else:
            plt.text(x, y, "  " + l_city + "( -" + str(l_count) + "- )", \
                fontweight=1000, ha='left', va='top', fontsize=5, color='Black');

        print(fg('orchid') + "MAP2: Mid-range investment focus:", \
                l_metro, l_city, l_count)
    elif int(l_count) > 9:
        plt.figure(3)
        c_state = metro_state_info[l_city]
        state_map3.append(c_state)

        # Get the location of city and plot it
        loc = geolocator.geocode(l_city)
        x, y = map3(loc.longitude, loc.latitude)
        map3.plot(x,y,marker='o',color='Red', \
                markersize=int(math.sqrt(l_count))*scale)
        if l_city == 'Bangalore':
           plt.text(x, y, "  " + l_city + "( -" + str(l_count) + "- )", \
                fontweight=1000, ha='right', va='top', fontsize=5, color='Black');
        else:
           plt.text(x, y, "  " + l_city + "( -" + str(l_count) + "- )", \
                fontweight=1000, ha='left', va='top', fontsize=5, color='Black');

        print(fg('orchid') + "MAP3: Low investment focus:", \
                l_metro, l_city, l_count)
    else:
        print("Not plotting")

print("########## Done plotting maps ###############")
print(state_map1)
print(state_map2)
print(state_map3)

plt.figure(1)
ax1 = plt.gca()
ax1.legend(loc='upper right', shadow=True, facecolor='#14a1ff', \
           fontsize='xx-small', title='CBIR: metros (development score)')
for nshape,seg in enumerate(map1.states):
    if state_names[nshape] in state_map1:
        poly = Polygon(seg,facecolor=l_facecolor1,edgecolor = c_border) # a dull orange
        ax1.add_patch(poly)

plt.title("India: high investment need zone", size = 7)
plt.savefig('output/HIN_zone.png', dpi=1200)


plt.figure(2)
ax2 = plt.gca()
ax2.legend(loc='upper right', shadow=True, facecolor='#14a1ff', \
           fontsize='xx-small', title='CBIR: metros (development score)')
for nshape,seg in enumerate(map2.states):
    if state_names[nshape] in state_map2:
        poly = Polygon(seg,facecolor=l_facecolor2,edgecolor = c_border) # a dull orange
        ax2.add_patch(poly)

plt.title("India: mid-range investment need zone", size = 7)
plt.savefig('output/MIN_zone.png', dpi=1200)

plt.figure(3)
ax3 = plt.gca()
ax3.legend(loc='upper right', shadow=True, facecolor='#14a1ff', \
           fontsize='xx-small', title='CBIR: metros (development score)')

for nshape,seg in enumerate(map3.states):
    if state_names[nshape] in state_map3:
        poly = Polygon(seg,facecolor=l_facecolor3,edgecolor = c_border) # a dull orange
        ax3.add_patch(poly)

plt.title("India: low investment need zone", size = 7)
plt.savefig('output/LIN_zone.png', dpi=1200)

print("########## Done coloring maps ###############")
plt.show()
