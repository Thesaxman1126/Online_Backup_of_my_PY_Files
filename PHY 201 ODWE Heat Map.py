import matplotlib.pyplot as plt
import numpy as np
import numpy.random as random
from datetime import datetime
start = datetime.now()
S = 100

def element(x,y,T,m):
    mc = 1
    value = 0
    while mc <= m:
        value += (2*T*(1-(-1)**mc)/(mc*np.pi*np.sinh(mc*np.pi)))*np.sin(np.pi*mc*x/S)*np.sinh(np.pi*mc*y/S)
        mc += 1
        
    return value

test_array = np.zeros([S,S])

for x in range(0,S):
    for y in range(0,S):
        test_array[y,x] = element(x,y,1,20)        

plt.imshow(test_array, cmap='turbo', interpolation='nearest')
plt.colorbar()
plt.ylabel("y (mm)")
plt.xlabel("x (mm)")
plt.title("Heat on 100mm x 100mm Metal Plate")
plt.show()

print('Tristin: ', datetime.now()-start)