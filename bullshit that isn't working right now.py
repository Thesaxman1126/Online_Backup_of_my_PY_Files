import scipy.special  
import numpy as np #Used for arrays and matrix like structures
import matplotlib.pyplot as plt #Used for plotting 
from mpl_toolkits.mplot3d import Axes3D #Used for some 3D-plotting 
from datetime import datetime #Used in runtime calculation
import matplotlib.animation as animation
#%matplotlib qt #RUN THIS IN CONSOLE BEFORE RUNNING CODE#

# CONSTANTS #
Re = 1 #Reynolds number 
dt = 1e-2 #Time step
dr = 1/5 #delta-r
dz = 1/5 #delta-z
Size = 5 #Size of matrix
Gamma = 1.5 #Aspect ratio
tolerance= 1e-5 #Min difference to test for steady state
r = np.linspace(0,1,Size)

# FUNCTIONS #
def l_2(v, nr = 50, nz = 50):
    
    v_norm_l = np.sqrt(1/((nr+1)*(nz+1)) * np.sum(v**2))
    return v_norm_l

def RHS(u):
    array = u[-1]
    for r in range(1,Size - 1):
        for z in range(1,Size - 1):
            a = (u[-1, r+1,z] - 2*u[-1,r,z] + u[-1,r-1,z]) / dr**2        
            b =  (u[-1,r+1,z] - u[-1,r-1,z]) / (2 * r * dr**2)
            c = - u[-1,r,z] / (r**2 * dr**2)
            d = (u[-1,r,z+1] - 2*u[-1,r,z] + u[-1,r,z-1]) / dz**2
            
            
            u[-1,r, z] = 1/Re * ( a + b + c +d)
        #print(a, '\n', b,'\n', c, '\n', d)
        #print(array[i,j])
    return u
    

def check(v0, v1, tol = tolerance):
    if l_2(v1) - l_2(v0) < tol:
        return True
    else:
        return False


v = np.zeros((1,Size,Size)) 
v[0, :,0] = r


print(v.shape[0])