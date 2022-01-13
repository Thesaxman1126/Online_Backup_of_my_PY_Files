# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 17:47:57 2021

@author: thesa
"""
import numpy as np
import matplotlib.pyplot as plt

lines = []
x = []
y = []
z = []

with open('Earth_horizons_results.txt') as f:
    lines = f.readlines()
    
c = 0


for line in lines:
    c += 1
    f_list = line.split(',')

    if len(f_list) == 12:
        if f_list[2] == '                      X':
            continue
        x.append(float(f_list[2]))
        y.append(float(f_list[3]))
        z.append(float(f_list[4]))
        
plt.plot(x,y)