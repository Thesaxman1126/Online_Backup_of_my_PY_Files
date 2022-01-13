# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 16:55:04 2021

@author: thesa
"""

import scipy.special
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# FUNCTIONS #
def v_test(r,z,gamma = 2.5):
    
    
    
    a= r*(1-z/gamma) 
    sums = 0
    
    for n in range(1,50):
        sums += ((scipy.special.iv(1,(n*np.pi*r)/gamma))/(n*scipy.special.iv(1,(n*np.pi)/gamma)))*np.sin(n*np.pi*z)    
    
    return a - (2/np.pi)*sums

#Contour plot
def plot_contour(Phi, filename=None, zlabel=r"potential $\Phi$ (V)",
                 cmap=plt.cm.coolwarm):
    """Plot Phi as a contour plot.
    
    Arguments
    ---------
    Phi : 2D array
          potential on lattice
    filename : string or None, optional (default: None)
          If `None` then show the figure and return the axes object.
          If a string is given (like "contour.png") it will only plot 
          to the filename and close the figure but return the filename.
    cmap : colormap
          pick one from matplotlib.cm          
    """
    fig = plt.figure(figsize=(5,4))
    ax = fig.add_subplot(111)

    x = np.arange(Phi.shape[0])
    y = np.arange(Phi.shape[1])
    X, Y = np.meshgrid(x, y)
    Z = Phi[X, Y]
    cset = ax.contourf(X, Y, Z, 20, cmap=cmap)
    ax.set_xlabel('r')
    ax.set_ylabel('z')
    ax.set_aspect(1)

    cb = fig.colorbar(cset, shrink=0.5, aspect=5)
    cb.set_label(zlabel)
    
    if filename:
        fig.savefig(filename)
        plt.close(fig)
        return filename
    else:
        return ax





# CONSTANTS/INITIALIZERS #
GAMMA = 2.5
Nmax = 100
Mmax = 100


vtest = np.zeros((Nmax,Nmax), dtype = np.float64 )

for r in range(Nmax):
    for z in range(Nmax):
        
        vtest[r][z] = v_test(1/(Nmax-1)*r,1/(Nmax-1)*z,gamma = 1)
        
        
#R-Diff tridiag matrix A_nn
A_nn = np.zeros((Nmax, Nmax), dtype=np.float64)

# WRITE DIAGONALS #
#A_nn
#Main
for i in range(Nmax): #Primary
    dr = 1/(Nmax)
    A_nn[i,i] = -(2+(1/((i+1)**2)))/(dr**2)

#Sub    
for i in range(Nmax-1):
    dr = 1/(Nmax)
    A_nn[i+1,i] = (1-1/(2*(i+1)))/(dr**2)
     
#Super
for i in range(Nmax-1):
    dr = 1/(Nmax)
    A_nn[i,i+1] = (1+1/(2*(i+1)))/(dr**2)
    
#Z_nn
eig, Z_nn = np.linalg.eig(A_nn)

inverseZ_nn = np.linalg.inv(Z_nn) #Z^(-1)

#F_nm
F_nm = np.zeros((Nmax, Mmax), dtype=np.float64)
for n in range(Nmax):
    dz = GAMMA / Mmax
    dr = 1/(Nmax)
    
    F_nm[n,0] = - (n+1) * (dr / (dz**(2)))

#Z-DIFF tridiag matrix B_mm 
B_mm = np.zeros((Mmax,Mmax), dtype = np.float64)

#B_mm
#Main
for j in range(Mmax):
    dz = GAMMA/(Mmax)
    
    B_mm[j,j] = -2/(dz**2)
    
#Sub
for j in range(Mmax-1):
    dz = GAMMA/(Mmax)
    
    B_mm[j+1,j] = 1/(dz**2)
    
#Super
for j in range(Mmax-1):
    dz = GAMMA/(Mmax)
    
    B_mm[j,j+1] = 1/(dz**2)


#H_mn array
H_mn = np.transpose(F_nm).dot(np.transpose(inverseZ_nn))

#Identiy of size m x m
I_mm = np.identity(Mmax)

#U_nm array
U_nm = np.zeros((Nmax, Mmax), dtype=np.float64)
for i in range(Mmax):
    U_nm[i,:] = np.linalg.inv(B_mm + eig[i]*I_mm).dot(H_mn[:,i])

u = inverseZ_nn.dot(vtest)
v = Z_nn.dot(U_nm)
plot_contour(v)
plot_contour(vtest)
