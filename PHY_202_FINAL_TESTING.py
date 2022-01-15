# add necessary imports
import numpy as np
import math
import matplotlib.pyplot as plt


# constants

G = 4*np.pi**2

mass = {
    'sun': 1.0,
    'earth': 3.0034e-6,
    'moon': 3.6923e-7}

r0 = {
    'sun': np.array([0,0,0]),
    'earth': np.array([9.978977040419635E-01, 6.586825681892025E-02, -6.320430920521123E-06]),
    'moon': np.array([9.956768547953816E-01, 6.676030485840675E-02, 1.641093070596718E-04])
     }
v0 = {
    'sun': np.array([0,0,0]),
    'earth': np.array([-4.70015711e-01, 6.25165839e+00, -3.40817831e-04]),
    'moon': np.array([-0.55065949, 6.03534661, 0.01111456])
}

# functions
def F_gravity(ri, rj, mi, mj):
    return -(G*mi*mj)/(np.linalg.norm(ri-rj))**2 *(ri-rj)/np.linalg.norm(ri-rj)

def F_ES(rE):
   return F_gravity(rE, r0['sun'], mass['earth'], mass['sun'])
   
def F_MS(rM):
    return F_gravity(rM, r0['sun'], mass['moon'], mass['sun'])

def F_EM(rE, rM):
    return F_gravity(rE, rM, mass['earth'], mass['moon'])

def F_ME(rE, rM):
    return F_gravity(rM, rE, mass['moon'], mass['earth'])

def  F_E(rE, rM):
    return F_ES(rE)+F_EM(rE, rM)

def  F_M(rE, rM):
    return F_MS(rM)+F_ME(rE, rM)   

def integrate_EM(tmax, dt=1e-3):
    t = 0
    rE = [r0['earth']]
    vE = v0['earth']
    rM = [r0['moon']]
    vM = v0['moon']
    
    while t < tmax:
        r_es = rE[-1]+vE*dt
        rE.append(r_es)
        r_ms = rM[-1]+vM*dt
        rM.append(r_ms)
        vE = vE +(1/mass['earth'])*F_E(rE[-1],rM[-1])*dt
        vM = vM +(1/mass['moon'])*F_M(rE[-1],rM[-1])*dt
        t = t+dt
    return(np.array(rE), np.array(rM)) 

if __name__ == "__main__":
    # create the trajectory for 1 year
    plt.xlabel('x (AU)')
    plt.ylabel('y (AU)')
    E,M = integrate_EM(1)
    plt.plot(E[:,0],E[:,1], label='Earth')
    plt.plot(M[:,0],M[:,1],'--' ,label='Moon')
    plt.legend(loc="best")
    plt.show()
    plt.savefig("orbit_earth_moon.png")
  
