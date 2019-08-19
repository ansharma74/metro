

'''
Filename: plot_sv150_t_bubble.py
Info: Anil Sharma (sharma_anil@yahoo.com); CBIR

Bubble plot of Sillicon Valley top 150 techs (Annual Rev ~$1 Trillion)


Input data:
    Input location info. file: datafiles/lonergan150_csv.csv

Usage example:
     ./plot_sv150_t_bubble.py

Output:
     Output file: output/silicon_valley_t150.png

'''

# Draw the locations of cities on a map of the US
# libraries
import matplotlib.pyplot as plt
import numpy as np
import csv

cmp_file = "datafiles/lonergan150_csv.csv"

cities = {}
cities = csv.DictReader(open(cmp_file, 'r'))


# create data
x =[]
y =[]
z =[]
color=[]
for rows in cities:
    if int(rows["Rank"]) < 151:
       x.append(rows["Rank"])
       color.append(int(rows["Rank"])/10)
       rev = int(rows["2018 Sales (M)"].replace(",","").strip("$"))/1000
       print(rev)
       y.append(rev)
       z.append(rows["Company"])
    # Change color with c and alpha. I map the color to the X axis value.
    
      #numfirms = len(y)


sum_y =sum(y)
print(sum_y)
sqr_shares = [(y/sum_y)**2 for y in y]
hhi_val = 10000*sum(sqr_shares)
      
print("HHI = %i" %(hhi_val))
    
plt.scatter(x, y, s=y, c=color, cmap="cool", alpha=0.7, edgecolors="grey", linewidth=3)
i = 0 
for x in x:
    if int(x) < 10:
        plt.text(int(x)+2,y[i]+2,z[i])
        i = i+1
plt.text(25,210, "Herfindahl-Hirschman Index Calculations")
plt.text(25,200, "SF Bay VC Community/Start Companies' HHI=%i" % (hhi_val))
if hhi_val < 1500:
   plt.text(25,190, "Highly Competitive")


plt.xticks([9,19,29,39,49,59,69,79,89,99,109,119,129,139,149])  
# Add titles (main and on axis)
plt.xlabel("SV 150 Ranks")
plt.ylabel("Revenue in $B")
plt.colorbar()
plt.tight_layout()

plt.title('SV 150 Revenue Bubble Chart (Rev. $B)', size = 7)

plt.savefig('output/sv_top150.png', dpi=1200, bbox_inches = 'tight',
    pad_inches = 0)

plt.show()
