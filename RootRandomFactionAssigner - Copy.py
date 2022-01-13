### ROOT RANDOM FACTION ASSIGNER ###
## IMPORTS ##
import random
#rom datetime import datetime

print("### WELCOME TO THE ROOT RANDOM FACTION ASSIGNER ###\n")
print("Press enter to start the assigner\n")
print("###################################################\n")
input()

## FUNCTIONS ##
# PRINT FOR A RANDOM MAP #
def print_dic_rand_map(mydic):
    maps = ['Original', 'Winter', 'Moutains', 'Lake']
    print()
    print("###################################################\n")
    for key, value in mydic.items() :
        print (f"{key}: {value}")
    print()  
    print(f'Your map is: {random.choice(maps)}')
    print('\nHave Fun :)')
    print()
    print("###################################################")

# PRINT FOR AN AGREED UPON MAP#
def print_dic(mydic):
    
    print()
    print("###################################################\n")
    for key, value in mydic.items() :
        print (f"{key}: {value}")
    print('\nHave Fun :)')
    print("###################################################")

# CHOOSE WHO GETS WHAT#
def choose(numPlayers, minNum, players_dic, players_list):
    
    i = 0 #Player indexer
    total = 0 #This is must be >= the min score
    
    #Instantiates dictionaries for initial run
    faction_values  = {
  
                      "Marquise de Cat": 10,
                      "Underground Dutchery": 8,
                      "Eyrie Dynasties ": 7,
                      "Vagabond (First)" : 5,
                      "Riverfolk Company" : 5,
                      "Woodland Alliance" : 3,
                      "Corvid Conspiracy" : 3,
                      "Vagabond (second)" : 2,
                      "Lizard Cult" : 2
                    
                    }
    
    faction_names  = {
                      
                      "Marquise de Cat" : "Marquise de Cat",
                      "Underground Dutchery" : "Underground Dutchery",
                      "Eyrie Dynasties " : "Eyrie Dynasties ",
                      "Vagabond (First)" : "Vagabond (First)",
                      "Riverfolk Company" : "Riverfolk Company",
                      "Woodland Alliance" : "Woodland Alliance",
                      "Corvid Conspiracy" : "Corvid Conspiracy",
                      "Vagabond (second)" : "Vagabond (second)",
                      "Lizard Cult" : "Lizard Cult"
                    
                      }
    # ATTEMPTS TO ASSIGN PLAYERS #
    while i < numPlayers:
        
        choice = random.choice(list(faction_names)) #This picks the player's faction
        total += faction_values[choice] #Adds the faction score to our sum
        players_dic[players_list[i]] = choice #Gives the player the random faction
        del faction_values[choice] #Takes away the faction from the pool
        del faction_names[choice] #Takes away the faction from the pool (Stops things from breaking)
        
        i += 1 #Next player
        
        # CHECKS IF THE ASSIGNMENT MEETS THE MINIMUM #
        if i == numPlayers:
            i = 0   #Reset index in case we have to re-run this process
            
            # CHECK THE SCORE #
            if total < minNum: #Case where we are less than the ROOT handbook's 
                i = 0 #Reset index (Just to make sure sometimes it broke here)
                total = 0 #Reset the faction score 
                players_dic = dict((k, None) for k in players_dic) #Reset who players got
    
                # REINSTANTIATING THE DICTIONARIES SINCE WE DELETED ENTRIES #
                faction_values  = {
  
                      "Marquise de Cat": 10,
                      "Underground Dutchery": 8,
                      "Eyrie Dynasties ": 7,
                      "Vagabond (First)" : 5,
                      "Riverfolk Company" : 5,
                      "Woodland Alliance" : 3,
                      "Corvid Conspiracy" : 3,
                      "Vagabond (second)" : 2,
                      "Lizard Cult" : 2
                    
                    }
                
                faction_names  = {
                      
                      "Marquise de Cat" : "Marquise de Cat",
                      "Underground Dutchery" : "Underground Dutchery",
                      "Eyrie Dynasties " : "Eyrie Dynasties ",
                      "Vagabond (First)" : "Vagabond (First)",
                      "Riverfolk Company" : "Riverfolk Company",
                      "Woodland Alliance" : "Woodland Alliance",
                      "Corvid Conspiracy" : "Corvid Conspiracy",
                      "Vagabond (second)" : "Vagabond (second)",
                      "Lizard Cult" : "Lizard Cult"
                    
                      }
                
                
            elif total >= minNum: #We meet the game criteria
                i = 100000 #Gets us outta the while loop
                return players_dic #Returns the players' assignments

if __name__ == '__main__':
    ## CONSTANTS AND INSTANTIATIONS ##
    #DICTIONARIES#
    # Dictionary for Players #
    player_Min_Num_dic = {
        
        "2" : 17,
        "3" : 18,
        "4" : 21,
        "5" : 25,
        "6" : 28
        
        }
    
    
    
    # CONTATNS #
    minNum = None
    
    #Players
    player = 1
    players_dic = {}
    players_list = []
    
    numPlayers = int(input('How many players are playing? '))
    
    if numPlayers < 2:
        raise Exception('Must have 2 players minimum. \nPlease rerun the code to try again')
    
    elif numPlayers > 6:
         raise Exception('6 players is the maximum.\nPlease rerun the code to try again')
        
    print('Who\'s playing? ')
    
    while len(players_dic) < numPlayers: 
        name = str(input(f'What is player {player}\'s name? '))
        players_dic[name] = None
        players_list.append(name)
        player += 1
    
    player = 1
      
    ## BRAINS ##
    rand_map = int(input("Do you want a random map? \n[1]: Yes\n[0]: No \n"))  
    if rand_map == 1:

        if numPlayers == 2:
            minNum = player_Min_Num_dic["2"]
            print_dic_rand_map(choose(numPlayers, minNum, players_dic, players_list))
       
        elif numPlayers == 3: 
            minNum = player_Min_Num_dic["3"]
            print_dic_rand_map(choose(numPlayers, minNum, players_dic, players_list))
        
        elif numPlayers == 4:
            minNum = player_Min_Num_dic["4"]
            print_dic_rand_map(choose(numPlayers, minNum, players_dic, players_list))
    
        elif numPlayers == 5: 
            minNum = player_Min_Num_dic["5"]
            print_dic_rand_map(choose(numPlayers, minNum, players_dic, players_list))
            
        elif numPlayers == 6:
            minNum = player_Min_Num_dic["6"]
            print_dic(choose(numPlayers, minNum, players_dic, players_list))
            print_dic_rand_map(choose(numPlayers, minNum, players_dic, players_list))
            
    else:

        if numPlayers == 2:
            minNum = player_Min_Num_dic["2"]
            print_dic(choose(numPlayers, minNum, players_dic, players_list))
            
        elif numPlayers == 3: 
            minNum = player_Min_Num_dic["3"]
            print_dic(choose(numPlayers, minNum, players_dic, players_list))
            
        elif numPlayers == 4:
            minNum = player_Min_Num_dic["4"]
            print_dic(choose(numPlayers, minNum, players_dic, players_list))
    
        elif numPlayers == 5: 
            minNum = player_Min_Num_dic["5"]
            print_dic(choose(numPlayers, minNum, players_dic, players_list))
    
        elif numPlayers == 6:
            minNum = player_Min_Num_dic["6"]
            print_dic(choose(numPlayers, minNum, players_dic, players_list))