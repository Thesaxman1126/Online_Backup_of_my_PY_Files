# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 01:11:57 2021

@author: thesa
"""
import random
import numpy as np

#FUNCTIONS#
#DICE ROLLING FUNCTIONS
def Roll_Die(): #Roll 1 die
    return random.randint(1,6)  
    
def Roll_Turn(Roll_num):
    if Roll_num == 1:
        roll_list1 = [Roll_Die()]
        print(roll_list1)
        return roll_list1 
    elif Roll_num == 2:
        roll_list2 = [Roll_Die(), Roll_Die()]
        print(roll_list2)
        return roll_list2
    elif Roll_num == 3:
        roll_list3 = [Roll_Die(), Roll_Die(), Roll_Die()]
        print(roll_list3)
        return roll_list3

    elif Roll_num == 4:
        roll_list4 = [Roll_Die(), Roll_Die(), Roll_Die(), Roll_Die()]
        print(roll_list4)
        return roll_list4

    elif Roll_num == 5:
        roll_list5 = [Roll_Die(), Roll_Die(), Roll_Die(), Roll_Die(), Roll_Die()]
        print(roll_list5)
        return roll_list5

    elif Roll_num == 6: #
        roll_list6 = [Roll_Die(), Roll_Die(), Roll_Die(), Roll_Die(), Roll_Die(), Roll_Die()]
        print(roll_list6)
        return roll_list6
    


#CHECKS
def Count_Roll(x):
    num1 = x.count(1)
    num2 = x.count(2)
    num3 = x.count(3)
    num4 = x.count(4)
    num5 = x.count(5)
    num6 = x.count(6)
    out = [num1, num2, num3, num4, num5, num6]
    print(out)
    return out

def End_Turn(x): #Turn End. Asks player if they scored. Input is the player index
    check = str(input('Did you score [y/n]? '))
    responses_yes = ['yes', 'y']
    responses_no = ['no', 'n']
    if check.lower() in responses_no:
        return 0
    elif check.lower() in responses_yes:
        return int(input(f'How much did {x} score? '))
    
#MENU
def Menu():
    print('Please make a selection')
    print('[1]: Roll 1 Die')
    print('[2]: Roll 2 Dice')
    print('[3]: Roll 3 Dice')
    print('[4]: Roll 4 Dice')
    print('[5]: Roll 5 Dice')
    print('[6]: Roll 6 Dice')
    print('[0]: End Turn/Frarkled')
    print('[-1]: End Game')

#INITIALIZERS#
#Players
player = 1
players = []

num_players = int(input('How many players are playing? '))
print('Who\'s playing? ')

while len(players) < num_players:    
    players.append(str(input(f'What is player {player}\'s name? ')))
    player += 1

player = 1
player_index = 0

#Scores
SCORES = []

while player <= num_players:
    SCORES.append(0)
    player += 1
player = 1

#LET'S PLAY FARKLE!
print()
print('The scores are set up as the following list')
print(SCORES)
print('The scores are in the following player order')
print(players)
print()
print('Let\'s play FARKLE!')

#To be sorted

x = 0

#BRAINS#
roll = None
while roll != -1:
    Menu()
    
    roll = (input(f'{players[player_index]}\'s selection: '))    
    if int(roll) == 1:
        print()
        print(f'{players[player_index]}\'s roll was')
        Roll_Turn(1)
        print()
    
    elif int(roll) == 2:
        print()
        print(f'{players[player_index]}\'s roll was')
        Roll_Turn(2)
        print()
    
    elif int(roll) == 3:
        print()
        print(f'{players[player_index]}\'s roll was')
        Roll_Turn(3)
        print()
    
    elif int(roll) == 4:
        print()
        print(f'{players[player_index]}\'s roll was')
        Roll_Turn(4)
        print()
    
    elif int(roll) == 5:
        print()
        print(f'{players[player_index]}\'s roll was')
        Roll_Turn(5)
        print()
   
    elif int(roll) == 6: 
        print()
        print(f'{players[player_index]}\'s roll was')
        Roll_Turn(6)
        print()
    
    elif int(roll) == 0:
        
        SCORES[player_index] += End_Turn(players[player_index])
        player_index += 1
        
        if player_index == num_players:
            print("Here are the scores so far")
            print(SCORES)
            player_index = 0
        
    elif int(roll) == -1:
        
        break
    
    else:
        print("ERROR try again")
    
    