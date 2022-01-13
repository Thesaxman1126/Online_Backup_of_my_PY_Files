# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 17:29:36 2021

@author: thesa
"""

import numpy as np
import matplotlib.pyplot as plt

def DDELTA(n,x):
    D_n = np.sqrt(n/np.pi) * np.exp(-n * x **2)
    return D_n

x = []

D_1 = []
D_2 = []
D_5 = []
D_10 = []
D_100 = []

i = -10
di = 1e-2
while i < 10:
    x.append(i)
    D_1.append(DDELTA(1,i))
    D_2.append(DDELTA(2,i))
    D_5.append(DDELTA(5,i))
    D_10.append(DDELTA(10,i))
    D_100.append(DDELTA(100,i))
    i += di

plt.plot(x, D_1, label = 'n = 1')
plt.plot(x, D_2, label = 'n = 2')
plt.plot(x, D_5, label = 'n = 5')
plt.plot(x, D_10, label = 'n = 10')
plt.plot(x, D_100, label = 'n = 100')
plt.legend()
plt.show()    