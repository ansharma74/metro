

'''
Filename: plot_sv150_t_bubble2_cir.py
Info: Anil Sharma (sharma_anil@yahoo.com); CBIR

Bubble plot of Sillicon Valley top 150 techs (Annual Rev ~$1 Trillion)


Input data:
    Input location info. file: datafiles/lonergan150_csv.csv

Usage example:
     ./plot_sv150_t_bubble2_cir.py

Output:
     Output file: output/sy_top150_cir.png

'''

# Draw the locations of cities on a map of the US
# libraries
import matplotlib.pyplot as plt
import numpy as np
import csv

cmp_file = "datafiles/lonergan150_csv.csv"

cmpy = {}
cmpy = csv.DictReader(open(cmp_file, 'r'))

ranks = 151
# create data
x =[]
y =[]
z =[]
sz =[]
color=[]
theta=[]
point=[]
for rows in cmpy:
    if int(rows["Rank"]) < ranks:
       x.append(rows["Rank"])
       theta.append(2 * np.pi * int(rows["Rank"]))
       point.append(int(rows["Rank"]))
       color.append(int(rows["Rank"])/10)
       y.append(int(rows["2018 Sales (M)"].replace(",","").strip("$"))/1000)
       sz.append(int(rows["2018 Sales (M)"].replace(",","").strip("$"))/100)
       z.append(rows["Company"])
       # Change color with c and alpha. I map the color to the X axis value.

theta.reverse()
point.reverse()
y.reverse()
z.reverse()
sz.reverse()
color.reverse()
#print(theta)
#print(point)
#print(y)
#print(z)
#print(color)
#print(sz)

fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')
c = ax.scatter(point, theta, c=color, s=sz, cmap='hsv', alpha=0.4)   
ax.set_rmax(ranks)

for ptr in point: 
    if ptr < 11:
        ax.annotate(z[ranks - ptr -1], xy=(point[ranks - ptr-1], theta[ranks - ptr-1]))
        
        
plt.title('SV 150 Revenue Bubble Chart (rev $B)', size = 7)

plt.savefig('output/sv_top150_cir.png', dpi=1200)

plt.show()
