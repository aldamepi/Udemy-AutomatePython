#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 09:15:04 2022

@author: albertomengual

Automate the Boring Stuff with Python:
Practice Projects of the Strings Chapter

"""

import zombiedice as zd




' TABLE PRINTER '.center(78, '#')
################################ TABLE PRINTER ###############################

# This function takes a list of lists of strings and dispays it in a 
# well-organized table with each column right-justified.
# Assume that all the inner lists will contain the same number of strings.




######### HINTS
# First find the longest string in each of the inner lists so that the whole
# column can be wide enough to fit all strings.

# You can create a list to store the width of the innerlists





######### INPUT

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]




def printTable(data):
    
    # Define an empty list for the max lenghts of the substrings
    colW = [0] * len(data)
    
    
    # Calculate the maximum length for each sublist
    for i1,sl in enumerate(data):
        maxLen = 0
        for st in sl:            
            if len(st) > maxLen:
                maxLen = len(st)
        colW[i1] = maxLen    
    #print(colW)

    # Display the table right adjusted (is a transposed matix)
    for i2 in range(len(data[0])):
        for i in range(len(data)):
            print(' ' + data[i][i2].rjust(colW[i]), end = ' ')
        print()
        


### EXECUTE
printTable(tableData)




########### TEXT CODE

# Print a list of sublists

# for i2 in range(len(data[0])):
#     for i in range(len(data)):
#         print(data[i][i2].rjust(colW[i]), end = '')
#     print()
    



' ZOMBIE DICE BOTS '.center(78, '#')
############################## ZOMBIE DICE BOTS ##############################

# Based on the code in myZombie.py write some bots to play Zombie Dice:
    # A bot that, after the first roll, randomly decides if it will continue
    # or stop
    
    # A bot that stops rolling after it has rolled two brains
    
    # A bot that stops rolling after it has rolled two shotguns
    
    # A bot that initially dicides it'll roll the dice one to four times,
    # but will stop early if it rolls two shotguns
    
    # A bot that stops rolling after it has rolled more shotguns than brains.

# The return value of zombiedice.roll() tells your code the results of the dice roll
# (it is a dictionary with four keys)

# If the bot has already rolled three shotguns, then the zombiedice.roll() will
# return none 




import zombiedice, random


class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}



        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN HERE:
        
        # Stops after it has rolled two brains
        # brains = 0
        # while diceRollResults is not None:
        #     brains += diceRollResults['brains']
        #     if brains < 2:
        #         diceRollResults = zombiedice.roll() # roll again
        #     else:
        #         break

        
        # Always roll its dice two times:
        # brains = 0
        # if diceRollResults is not None:
        #     brains += diceRollResults['brains']
        #     diceRollResults = zombiedice.roll() # roll again


        # After the first roll, randomly decides to continue
        #brains = 0
        # if diceRollResults is not None:
        #     #brains += diceRollResults['brains']

        #     if random.randint(0,1) == 1:
        #         diceRollResults = zombiedice.roll() # roll again
                
        
        # Stops rolling after two shotguns:
        # shotG = 0
        # while diceRollResults is not None:
        #     shotG += diceRollResults['shotgun']

        #     if shotG < 2:
        #         diceRollResults = zombiedice.roll() # roll again
        #     else:
        #         break
        
        
        # Initially dicides 1 to 4 rolls but stops rolling after two shotguns:
        # shotG = 0
        # nRolls = random.randint(1,4)
        # count = 1
        # while diceRollResults is not None and count < nRolls:
        #     shotG += diceRollResults['shotgun']

        #     if shotG < 2:
        #         diceRollResults = zombiedice.roll() # roll again
        #         count += 1
        #     else:
        #         break
        
        
        # Stops after it has rolled more shotguns than brains:
        shotG = 0
        brains = 0
        while diceRollResults is not None:
            shotG = diceRollResults['shotgun']
            brains = diceRollResults['brains']
            
            if shotG <= brains:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break
            


zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Until 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Until 1 Shotgun', minShotguns=1),
    MyZombie(name='My Zombie Bot'),
    MyZombie('Alberto')
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
zombiedice.runTournament(zombies=zombies, numGames=1000)
#zombiedice.runWebGui(zombies=zombies, numGames=1000)


























































































