#!/usr/bin/python3

'''
Filename: geopy_india_metros_edu.py
Info: Anil Sharma (sharma_anil@yahoo.com); CBIR

Draw education cities locations on a map of India.
Mark presence of IITs(T), IIMs(M) and Top Med Schools(H) with Metro Size Marker

Input data:
    Map-files: map_files/gadm36_IND_1 
               map_files/gadm36_IND_1 
               map_files/gadm36_IND_1
    Input location info. file: datafiles/City_Metro_data.csv

Usage example:
     ./geopy_india_metros_edu.py

Output:
     Output map-gif file: output/ind_edu_cities.png

'''

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap as Basemap
from geopy.geocoders import Nominatim
from matplotlib.patches import Polygon
import matplotlib.lines as mlines
import math
import csv
from colored import fg

plt.figure(num=1, figsize=(8,6), facecolor='#fffbe5', edgecolor='blue')

#City Database file
city_file = "datafiles/City_Metro_data.csv"

cities = {}
cities = csv.DictReader(open(city_file, 'r'))

scale = 2
c_border = '#808cff' # Light blue

map = Basemap(llcrnrlon=69,llcrnrlat=7,urcrnrlon=99,urcrnrlat=35, \
                projection='lcc', lon_0 = 77, lat_0 = 22, resolution='f')
# load the shapefile, use the name 'states'
map.readshapefile('map_files/gadm36_IND_1', name='states', \
                drawbounds=True, color = c_border)
map.drawcountries(linewidth=0.2, linestyle='solid', color = c_border)
map.drawcoastlines(linewidth=0.2, linestyle='solid', color = c_border)

ax = plt.gca() # get current axes instance
for nshape,seg in enumerate(map.states):
    poly = Polygon(seg,facecolor='#ffAA7C',edgecolor = c_border) # dull orange
    ax.add_patch(poly)

# Get the location of each city and plot it
geolocator = Nominatim()
for rows in cities:
    l_metro = rows["Metro Area"]
    l_city = rows["Main City"]
    l_count = rows["Score(12)"]
    l_IIM = int(rows["IIM"])
    l_IIT = int(rows["IIT"])
    l_Med = int(rows["Med"])
    loc = geolocator.geocode(l_city)
    x, y = map(loc.longitude, loc.latitude)

    # City Size Marker
    if int(l_count) <= 6:
        map.plot(x,y,marker='P',color='white', \
            markersize=int(math.sqrt(int(l_count)))*scale)
    elif int(l_count) <= 9:
        map.plot(x,y,marker='s',color='#cfe2d4', \
            markersize=int(math.sqrt(int(l_count)))*scale)
    else:
        map.plot(x,y,marker='D',color='cyan', \
            markersize=int(math.sqrt(int(l_count)))*scale)

    # City Name
    if l_city == 'Bangalore':
        plt.text(x, y, l_city + "(-" + l_count + "-)" + "    ", \
            fontweight=1000,ha='right', va='bottom', fontsize=6, color='Black')
    elif l_city == 'Ahmedabad':
        plt.text(x, y, " " + l_city + "(-" + l_count + "-)", \
            fontweight=1000,ha='center', va='bottom', fontsize=6, color='Black')
    else:
        plt.text(x, y, "    " + l_city + "(-" + l_count + "-)", \
            fontweight=1000,ha='left', va='bottom', fontsize=6, color='Black')

    # Institutes
    if l_Med == 1:
        plt.text(x, y, "Med", fontweight=1000, ha='center', \
                            va='center', fontsize=5, color='Green')
    if l_IIM == 1:
        plt.text(x, y, "   Biz", fontweight=1000, ha='left', va='top', \
                            fontsize=5, color='Blue')
    if l_IIT == 1:
        plt.text(x, y, "Tech   ", fontweight=1000, ha='right', \
                            va='top', fontsize=5, color='Red')

    print(fg('orchid') + "MAP - EDU centers:",l_metro,",", \
                         l_city,",",l_count,",",l_Med,",",l_IIM,",",l_IIT)

print("########## Done plotting MAP ###############")
print("########## Legends #####################")
white_cross = mlines.Line2D([], [], color='white', marker='P', linestyle='None',
                          markersize=5, label='Small Metros (Score up to 6)')
cream_square = mlines.Line2D([], [], color='#cfe2d4', marker='s', 
         linestyle='None', markersize=5, label='Mid-Size Metros (Score 7 to 6)')
cyan_diamond = mlines.Line2D([], [], color='cyan', marker='D', linestyle='None',
                          markersize=5, label='Large Metros (Score 10 to 12)')
legend1 = plt.legend(handles=[white_cross, cream_square, cyan_diamond], 
           title='Metro Ranks (CBIR)', loc='upper right' , \
           facecolor = 'purple', fontsize=7, fancybox=True)

tech = mlines.Line2D([], [], color='Red', marker='$T$', linestyle='None',
                          markersize=5, label='Top technical institute')
biz = mlines.Line2D([], [], color='Blue', marker='$B$',linestyle='None',
                          markersize=5, label='Top business school')
med = mlines.Line2D([], [], color='Green', marker='$M$', linestyle='None',
                          markersize=5, label='Top medical college')
legend2 = plt.legend(handles=[tech, biz, med], title='EDU Centers (CBIR)',
           loc='lower right' , facecolor = 'orange', fontsize=7, fancybox=True)

legend1.get_title().set_fontsize('10')
legend2.get_title().set_fontsize('10')
ax.add_artist(legend1)
ax.add_artist(legend2)

plt.title("Top education destinations: India", size = 7)

plt.savefig('output/ind_edu_cities.png', dpi=1200)

plt.show()
