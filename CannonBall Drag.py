# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 13:22:25 2021

@author: thesa

models the trajectory of a cannon ball with different drags
"""

import numpy as np
import matplotlib.pyplot as plt


def Rey_Num(rho, L, v, eta):
    return (rho *L * v) / eta

def Lin_Drag_Force(eta, L, v):
    return 3 * np.pi * eta * L *v

def Quad_Drag_Force(k, rho, A, v):
    return k * rho * A * v**2

def Lin_Drag_Velo(eta, L, v):
    return None

def Quad_Drag_Velo(k, rho, A, v):
    return None

def Lin_Drag_Pos(eta, L, v):
    return None

def Quad_Drag_Pos(k, rho, A, v):
    return None

#INITIALIZERS#
#Positionl arrays
#vacuum
x_pos_vac = []
y_pos_vac = []

#Lin drag
x_pos_lin = []
y_pos_lin = []

#Combo drag
x_pos_quad = []
y_pos_quad = []

#Initial conditions
x = 0 #x position 
y = 0 #y position
t = 0 #initial time
dt = 1e-3 #time step

#No Drag
while y >= 0:
    y = -t*(t-10)
    x = t
    x_pos_vac.append(y)
    x_pos_vac.append(x)
    t += dt

y = 0
#Linear Drag
while y >= 0:
    break

y = 0
#Newtonian + Linear Drag
while y >= 0:
    break

plt.plot(x_pos_vac, y_pos_vac)
plt.show()