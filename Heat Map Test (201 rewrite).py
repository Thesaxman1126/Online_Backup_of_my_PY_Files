# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 03:50:42 2021

@author: thesa
"""

import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
start = datetime.now()
i = 0
j = 0
dt = 1e-1


T_0 = 1#float(input('Initial Temperature: '))
S = 10#float(input('Length of side: '))
m = 20#int(input('number of terms (int): '))

def Temp(x,y):
    k = 1
    temp = 0
    while k <= m:
        a = (1 - (-1)**k)
        b = k * np.pi * np.sinh(k*np.pi)
        c = np.sin(((k*np.pi)/S)*x)
        d = np.sinh((k*np.pi)/S*y)
        temp += (a / b) * c * d
        k += 1
    return 2*T_0 * temp

x = []
y = []
z = []

while i < 10:
    j = 0
    while j < 10:
        x.append(i)
        y.append(j)
        z.append(Temp(i,j))
        
        j += dt        
    i += dt


fig = plt.figure()
ax = fig.add_subplot(111)
img = ax.scatter(x, y, c=z, cmap='turbo')
fig.colorbar(img)
plt.show()

print('Nick: ', datetime.now()-start)