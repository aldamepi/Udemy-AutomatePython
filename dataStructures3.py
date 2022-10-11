#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 23:16:57 2022

@author: albertomengual
"""


# DATA STRUCTURES PRACTICE 3



############### FANTASY GAME INVENTORY #################

# Dictionary to model the player's inventory:
    # Keys: str describing the item in the inventory
    # Value: int how many of each item

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


####### INTRUCTIONS

# Write a function named displayInventory() that would take any posible
# inventory and display it like the following:
    # Inventory:
    # value1 key1
    # value2 key2 
    # value3 key3
    # .....
    # Total number of items: int





######## CODE

# Create a function that print the inventory dictionary 
# Create a function that sums al the values




# Print inventory

def printInventory(inv):
    print('Inventory:')
    for k,v in inv.items():
        print(str(v) + ' ' + k)



# Sum items

def sumItems(inv):
    count = sum(inv.values())
    return count




# Main function

def displayInventory(inv):
    printInventory(inv)
    print('Total number of items: ' + str(sumItems(inv)))



displayInventory(inventory)





# DATA STRUCTURES PRACTICE 4



############### LIST TO DICTIONARY FUNCTION #################
################# FANTASY GAME INVENTORY ####################

# Add a given loot to the inventory

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# Main function addToInventory(inv, addIt):
    # inv parameter: a dictionary representing the player's inventory.
    # addit parameter: is a list representing a loot
# It should return a dictionary that represents the updated inventory

inventory2 = {'gold coin': 42, 'rope': 1}



############# ALGORITHM

# create a function that turns the loot into a dictionary
# create a function that updates the inventory2 with the loot dictionary:
    # creates new keys and values or sum new values to existing keys
    # return the new inventory








# Function List to Dictionary

def listToDict(loot):
    inv = {}
    for x in loot:
        inv.setdefault(x, 0)
        inv[x] += 1
    
    return inv


# newInv = listToDict(dragonLoot)




# Update inventory

def updInventory(inv,lootInv):
    for k,v in lootInv.items():
        inv.setdefault(k, 0)
        inv[k] += v
    return inv





# Main function

def addToInventory(inv,addIt):
    newInv = {}
    newInv = listToDict(addIt)
    return updInventory(inv,newInv)
    

displayInventory(inventory2)

inventory2 = addToInventory(inventory2,dragonLoot)

displayInventory(inventory2)
    





# Test Code





































































































