# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 00:25:44 2021

@author: thesa
"""

# importing csv module
import csv
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
input('Press enter to start')
# csv file name
filename = "Testdata2.csv"
  
# initializing the titles and rows list
fields = []
rows = []
x = []
y = []
z = []
c = []
# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
      
    # extracting field names through first row
    fields = next(csvreader)
  
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

i = 0
for i in range(0, len(rows)):
    x.append(float(rows[i][0]))
    y.append(float(rows[i][1]))
    z.append(float(rows[i][2]))
    c.append(np.sin((float(rows[i][3]))))
#print(x)
#print(y)
#print(z)
#print(c)    
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

img = ax.scatter(x, y, z, c=c, cmap='turbo')
fig.colorbar(img)
input('Press enter to see graph')
plt.show()