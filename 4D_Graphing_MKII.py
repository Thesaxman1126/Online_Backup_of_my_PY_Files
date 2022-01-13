#IMPORTS#
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
start = datetime.now()
#INITIAL LIST#
x = []
y = []
z = []
c = []
#INITIALIZERS#
i = 0
j = 0
#"TIME STEP"#
dt = 1e-1
#FUNCTIONS#
#FIND Z#
def Z_Value(x,y):
    return np.cos(x)-np.sin(y)
#    return np.exp(-0.1*y)*np.cos(x)-np.exp(-0.1*x)*np.sin(y)
#GIVE COLOR#
def Color_Value(x,y,z):
    return np.sqrt(x**2+y**2+z**2) 
#POPULATE LISTS#
while i < 10:
    j = 0
    while j < 10:
        x.append(i)
        y.append(j)
        z.append(Z_Value(i,j))
        c.append(Color_Value(i, j, Z_Value(i,j)))
        j += dt        
    i += dt
#PLOT#
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
img = ax.scatter(x, y, z, c=c, cmap='turbo')
fig.colorbar(img)
plt.show()
print(datetime.now()-start)