#IMPORTS#
import numpy as np
import itertools
from datetime import datetime

#FUNCTIONS#
#MENU#
def Menu():
    print("Please choose an option")
    print("[1]: Test All Permutations (Does not support repeating indicies)")
    print("[2]: Test A Single Permutations (Supports repeating indicies)")
#    print("[3]: See How Many Calculations Are Done When Testing All Permutations")
    print("[0]: Quit Program")

#SIGN FN#
def Sgn(x):
    if x != 0:
        return x / abs(x)
    else:
        return 0
    
#PERMUTATION TESTER#
def Test_permutation(z,y):
    if y == 1:
        print(z, ": EVEN(+1)")
    elif y == -1:
        print(z, ": ODD (-1)")
    elif y == 0:
        print(z, "NONE (0)")
    else:
        print("ERROR SOMETHING WENT WRONG.")

#VANDERMONDE DET CALCULATION#
def Vand_Det(w):
    return np.linalg.det(w)

#FACTORIAL CALCULATION#
def Factorial(a):
    fact = 1
    for j in range(1,a+1):
        fact = fact * j
    return fact

#START-UP#
print("### Welcome to the Levi-Civita program writen by Nick Navas ###")
Menu()
option = int(input("What would you like to do? "))

#MENU LOOP#
while option != 0:
    if not type(option) is int:
        print(0)
    #ALL PERMUTATIONS#
    if option == 1:
        print()
        #GET INDEX NUMBER#
        numIndex = int(input("Number of indicies to permute (note: is starts to lag at n = 9): "))
        
        #INITIALIZERS#
        i = 1
        LEVI = []
        start1 = datetime.now()

        
        #Test print      
        print("There are", Factorial(numIndex), "permutations")
        print("there are", int(Factorial(numIndex)), "even permutations (+1)\nthere are", int(Factorial(numIndex)), "odd permutations (-1)" )
        print()
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
        for k in range(0,Factorial(numIndex)):
            CIVITA = []
            for l in range(0,numIndex):
                CIVITA.append(LEVI[k][l])
            VANDER = np.vander(CIVITA, increasing=True)
            Test_permutation(CIVITA, Sgn(Vand_Det(VANDER)))
        print("###########################################################################")
        print()
        print("############################ CALCULATIONS DONE ############################")
        print("Num of matricies set up: ", Factorial(numIndex))
        print("Num of calculations per matrix", numIndex**2)
        print("Total calculations (Num Matrix * calc/Matrix): ", Factorial(numIndex) * numIndex**2)
        print("Runtime", datetime.now()-start1)
        print("###########################################################################")
    #SINGLE TEST#
    elif option == 2:
        print()
        #INTIALIZERS#
        num = 1
        LEVI2 = []
        numIndex2 = int(input("Number of indicies to permute: "))
        start2 = datetime.now()
        #MAKES THE LIST/VANDERMONDE MATRIX#
        while len(LEVI2) < numIndex2:
            x = int(input("Index #{} ".format(num) ))
            num = num + 1
            LEVI2.append(x)
        VANDER2 = np.vander(LEVI2, increasing=True)
        
        #PRINT RESULTS#
        print()
        print("############################### HERE YOU GO ###############################")
        Test_permutation(LEVI2, Sgn(Vand_Det(VANDER2)))
        print("Runtime", datetime.now()-start2)
        print("###########################################################################")
        print()
    
    elif option == 69:
        print()
        print("nice")
        #print()
    #INVALID INPUTS#
    else:
        print()
        print("INVALID SELECTION PLEASE TRY AGAIN")
    
    #RELOADS MENU AFTER SELECTION#    
    print()
    Menu()
    option = int(input("What would you like to do? "))


#CLOSING THE PROGRAM#
print("Thank you! Have a good day.")