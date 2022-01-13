#IMPORTS#
#from sympy import Eijk, LeviCivita
import numpy as np
import itertools

#FUNCTIONS#
#SIGN FN#
def Sgn(x):
    return x / abs(x)

#PERMUTATION TESTER#
def Test_permutation(z,y):
    if y == 1:
        print(z, ": EVEN(+1)")
    elif y == -1:
        print(z, ": ODD (-1)")
    else:
        print("ERROR SOMETHING WENT WRONG.")
        

#GET INDEX NUMBER#
numIndex = int(input("Number of indicies to permute (note the limit is n = 10): "))

#INITIALIZERS#
i = 1
fact = 1
LEVI = []

#FACTORIAL CALCULATION#
for j in range(1,numIndex+1):
    fact = fact * j

#Test print      
print("There are", fact, "permutations")
print("there are", int(fact/2), "even permutations (+1)\nthere are", int(fact/2), "odd permutations (-1)" )
print("################### HERE ARE THE FOLLOWING PERMUTATIONS ###################")


#FILL LIST WITH INDEICIES#
while i <= numIndex:
    LEVI.append(i)
    #TEST PRINTING#
    #print(i)
    i = i+1
    
#PERMUATOR#
LEVI = list(itertools.permutations(LEVI))

#READ TUPLES/THROW RESULTS INTO FUNCTIONS#
for k in range(0,fact):
    CIVITA = []
    for l in range(0,numIndex):
        CIVITA.append(LEVI[k][l])
    VANDER = np.vander(CIVITA, increasing=True)
    Test_permutation(CIVITA, Sgn(np.linalg.det(VANDER)))
print("###########################################################################")