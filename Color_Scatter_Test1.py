with open("4D_Test_Data.txt") as mytxt:
    for line in mytxt:
        print (line)
    
        #Or do something with line
    
        # if you want to split the line
        # assuming data is tab separated
        newline = line.rstrip("\n").split("\t")
    
        # if you want conditional printing
        if len(line) > 0:
            print(line)