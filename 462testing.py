# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 22:31:00 2021

@author: thesa
"""
## IMPORTS ##
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# FUNCTIONS #
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
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_aspect(1)

    cb = fig.colorbar(cset, shrink=0.5, aspect=5)
    cb.set_label(zlabel)
    
    if filename:
        fig.savefig(filename)
        plt.close(fig)
        return filename
    else:
        return ax



## INITIATIZING ARRAYS AND CONSTANTS ##
gamma = 1.0 #float(input("Value for Gamma: "))

gammaSize = int(gamma *100+ 1)

#Used for array sizes
Nmax = 100
Mmax = 100
#Max_iter = 70

#Indexes (These will constantly reset)
i = 0
j = 0
k = 0

# ARRAYS #
#R-Diff tridiag matrix A_nn
A_nn = np.zeros((Nmax, Nmax), dtype=np.float64)

# WRITE DIAGONALS #
#A_nn

while i < Nmax: #Primary
    dr = 1/(i+1)
    A_nn[i,i] = -(2+1/(i+1)**2)/dr**2
    i += 1
i = 0


while i < Nmax-1: #Sub
    dr = 1/(i+1)
    A_nn[i+1,i] = (1-1/(2*(i+1)))/(dr**2)
    i += 1 
i = 0

#Super
while i < Nmax-1:
    dr = 1/(i+1)
    A_nn[i,i+1] = (1+1/(2*(i+1)))/(dr**2)
    i += 1 
i=0
print("#################HERE IS A_nn\n",A_nn,"\n#################\n") 


#Diagonal transform
Z_nn, Z_nn = np.linalg.eig(A_nn) #Makes matrix for Z_nn
inverseZ_nn = np.linalg.inv(Z_nn) #Z^(-1)
E_nn= inverseZ_nn.dot(A_nn).dot(Z_nn) #Z^(-1).A.Z
eig = np.linalg.eig(A_nn)
e_i = eig[0]


#Z-Diff tridiag matrix B_mm
B_mm = np.zeros((Mmax, Mmax), dtype=np.float64)
while j < Mmax:
    dz = gamma / (j+1)
    B_mm[j,j] = -2/dz**2
    j += 1
j = 0
while j < Mmax-1:
    dz = gamma / (j+1)
    B_mm[j+1,j] = 1/dz**2
    j += 1
j = 0
while j < Mmax-1:
    dz = gamma / (j+1)
    B_mm[j,j+1] = 1/dz**2
    j += 1

print("#################HERE IS B_mm\n",B_mm,"\n#################\n") 

#RHS ARRAY F_nm
F_nm = np.zeros((Nmax, Mmax), dtype=np.float64)
   
while k <= Nmax -1:
    #F_nm[-1,k] = F_nm[-1,k] + 1/(Nmax-1)*k
    dz = gamma / (1)
    dr = 1/(k+1)
    
    F_nm [k,0] = F_nm [k,0] - dr*(1+k)/dz**2
    
    k+=1
k = 0

#H_mn array
H_mn = np.transpose(F_nm).dot(np.transpose(inverseZ_nn))

#Identiy of size m x m
I_mm = np.identity(Mmax)

#U_nm array
U_nm = np.zeros((Nmax, Mmax), dtype=np.float64)
i=0
while i < Mmax-1:
    U_nm[i,:] = np.linalg.inv(B_mm + e_i[i]*I_mm).dot(H_mn[:,i])
    i += 1


# BOUNDARY CONDITIONS #

#0 conditions
#v = np.zeros((Nmax, Mmax), dtype=np.float64)
#v[0, :] = 0   #(0,0) -> (0,gamma) =0 /\ (0,gamma) -> (1,gamma) = 0 /\ (1,0) -> (1,gamma) =0 
k = 0

#NH Conditions
#Loop sets the (0,0) -> (1,0) boundary condition
#while k <= Mmax -1:
#    v[-1,k] = v[-1,k] + 1/(Nmax)*k

 #   k+=1
#k = 0 #reset indexing in case I need it
#print(v)
print(F_nm)















#U_nm = rows of the solution (B_mm +eigenvalues I_mm)



#v = Z_nn * U_nm
v = Z_nn.dot(U_nm)

print(v)



plot_contour(v)