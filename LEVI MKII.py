from sympy import Eijk, LeviCivita
import numpy as np

a = 1 
b = 1 
c = 1
d = 1

while a == 1:
    LEVI = Eijk(a,b,c,d)
    if LEVI == 1:
        print(a,b,c,d,": even" )
    elif LEVI == -1:
        print(a,b,c,d,": odd" )
    elif LEVI == 0:
        print("NONE")
    else:
        print("BROKEN")