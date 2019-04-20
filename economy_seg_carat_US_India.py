#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
 
Y_IND = ('US 1990', 'India 1990', 'China_1990', 'US 2020', 'India 2020', 'China_2020')

y = np.arange(len(Y_IND))

Economy = ('Agri-business', 'Hospitality retail support', 
       'Manufactung industry', 'High-end services', 'Knowledge economy')
segments = np.arange(len(Economy))

#US_1990 = (20, 25, 35, 10, 10)
#India_1990 = (60, 15, 15, 5, 5)
#China_1990 = (33, 13, 45, 5, 5)

#US_2020 = (20, 20, 20, 20, 20)
#India_2020 = (40, 20, 15, 15, 10)
#China_2020 = (10, 20, 40, 20, 10)

# generate some multi-dimensional data & arbitrary labels
data = [[20, 60, 32, 20, 40, 10], [25, 15, 13, 20, 20, 20], [35, 15, 45, 20, 15, 40], 
       [10, 5, 5, 20, 15, 20], [10, 5, 5, 20, 10, 10]]
percentage = [[20, 25, 35, 10, 10], [60, 15, 15, 5, 5], [32, 13, 45, 5, 5],
        [20, 20, 20, 20, 20], [40, 20, 15, 15, 10], [10, 20, 40, 20, 10]]


y_pos = np.arange(len(Y_IND))

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)

colors ='rgbmc'
patch_handles = []

left = np.zeros(len(Y_IND)) # left alignment of data starts at zero

d_bar = {"capstyle": "round", "joinstyle": "bevel", "rasterized": "TRUE"}

for i, d in enumerate(data):
    patch_handles.append(ax.barh(y_pos, d, height=0.8,
         color=colors[i%len(colors)], align='center', left=left, edgecolor='black', **d_bar))
    # accumulate the left-hand offsets
    left += d

# go through all of the bar segments and annotate
for j in range(len(patch_handles)):
    for i, patch in enumerate(patch_handles[j].get_children()):
        bl = patch.get_xy()
        x = 0.5*patch.get_width() + bl[0]
        y = 0.5*patch.get_height() + bl[1]
        ax.text(x,y, "%d%%" % (percentage[i][j]), ha='center', color='w', fontsize=12, fontweight='black')

ax.set_yticks(y_pos)
ax.set_yticklabels(Y_IND, fontsize=12, fontweight='black')
ax.set_xlabel(Economy, fontsize=12, fontweight='black')
ax.set_title(" ---------- Economic and Social Development Levels ----------->" , fontsize=12, fontweight='black')
plt.savefig("econ_gr.png",type="png",dpi=300)
# Show graphic
plt.show()

