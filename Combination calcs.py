from itertools import combinations
 
# Get all combinations of [1, 2, 3]
# and length 2
comb = combinations([1, 2, 3,4,5,6], 1)
c = 1
# Print the obtained combinations
for i in list(comb):
    print (c,' : ',i)

    c += 1