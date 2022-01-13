# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 17:25:18 2021

@author: thesa
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# %matplotlib inline
#%matplotlib notebook

Nmax = 100
Max_iter = 70
Phi = np.zeros((Nmax, Nmax), dtype=np.float64)

# initialize boundaries
# everything starts out zero so nothing special for the grounded wires
Phi[0, :] = 100   # wire at x=0 at 100 V
i=0
#while i <= 100:
#    Phi[-1,i] = Phi[-1,i] + 1/(Nmax-1)*i
#    i+=1
# Jacobi: do not change the potential during one update, so we need to work on a copy
Phi_new = Phi.copy()
print(Phi)
Nx, Ny = Phi.shape
for n_iter in range(Max_iter):
    for xi in range(1, Nx-1):
        for yj in range(1, Ny-1):
            Phi_new[xi, yj] = 0.25*(Phi[xi+1, yj] + Phi[xi-1, yj] 
                                 + Phi[xi, yj+1] + Phi[xi, yj-1])
    # update the potential for the next iteration
    Phi[:, :] = Phi_new


# plot Phi(x,y)
x = np.arange(Phi.shape[0])
y = np.arange(Phi.shape[1])
X, Y = np.meshgrid(x, y)

Z = Phi[X, Y]
print(Z)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(X, Y, Z, rstride=2, cstride=2)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel(r'potential $\Phi$ (V)')

ax.view_init(elev=40, azim=-65)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_wireframe(X, Y, Z, rstride=2, cstride=2, linewidth=0.5, color="gray")
surf = ax.plot_surface(X, Y, Z, cmap=plt.cm.coolwarm, alpha=0.6)
cset = ax.contourf(X, Y, Z, zdir='z', offset=-50, cmap=plt.cm.coolwarm)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel(r'potential $\Phi$ (V)')
ax.set_zlim(-50, 100)
ax.view_init(elev=40, azim=-65)

cb = fig.colorbar(surf, shrink=0.5, aspect=5)
cb.set_label(r"potential $\Phi$ (V)")