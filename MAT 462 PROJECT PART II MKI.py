# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 22:31:00 2021

@author: thesa
"""
## IMPORTS ##
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

## INITIATIZING ARRAYS AND CONSTANTS ##
gamma = 1#float(input("Value for Gamma: "))

gammaSize = gamma * 100 +1

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

#RHS ARRAY#
#RHS ARRAY F_nm
F_nm = np.zeros((Nmax, Mmax), dtype=np.float64)

k = 0
while k <= Nmax -1:
    #F_nm[-1,k] = F_nm[-1,k] + 1/(Nmax-1)*k
    dz = gamma
    dr = 1/(k+1)
    
    F_nm [k,0] = - dr*(k+1)/dz**2
    
    k+=1
k = 0

#H_mn array
H_mn = np.transpose(F_nm).dot(np.transpose(inverseZ_nn))

U_nm = np.zeros((Nmax, Mmax), dtype=np.float64)
I_mm = np.identity(Mmax)


# BOUNDARY CONDITIONS #

#0 conditions
v = np.zeros((Nmax, Mmax), dtype=np.float64)
v[0, :] = 0   #(0,0) -> (0,gamma) =0 /\ (0,gamma) -> (1,gamma) = 0 /\ (1,0) -> (1,gamma) =0 
k = 0

#NH Conditions
#Loop sets the (0,0) -> (1,0) boundary condition
while k <= Mmax -1:
    v[-1,k] = v[-1,k] + 1/(Nmax)*k

    k+=1
k = 0 #reset indexing in case I need it
print(v)
print(F_nm)















#U_nm = rows of the solution (B_mm +eigenvalues I_mm)\mathbf{u_i} = \mathbf{h_i}



#v = Z_nn * U_nm




# Plotting #
x = np.arange(v.shape[0])
y = np.arange(v.shape[1])
X, Y = np.meshgrid(x, y)

Z = v[X, Y]

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

#