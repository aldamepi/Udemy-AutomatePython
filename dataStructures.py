#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 13:13:54 2022

@author: albertomengual
"""


# DATA STRUCTURES PRACTICE

# Given a dictionary with nested dictionaries as values:
    # The main dicitionary keys are names of people
    # The main values are nested dictionaries with things as keys and amount
    # of those things as values

# Obtain the total amount of each thing in the nested dictionaries

# The names of the people are not returned


################# Algorithm ###################

# ????? Create a list of the things?
# Create a loop to check every nested dictionary and sum the amount to each key.





# Input Dictionary

allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}} 



# Code Tests


for k,v in allGuests.items():
    print(v)
    
    
for v in allGuests.values():
    print(v)

for v in allGuests.values():
    print(v.get('apples',0))



# el siguiente codigo está mál:
# el foco se encuentra en la función get. 
# La función get es la que devuelve el valor para una clave del diccionario.
# Siempre que exista la clave.
# Cada clave esta como mucho una vez en cada diccionario
# El diccionario (anidado) al que se pasa dicha funcion es el valor del 
# diccionario principal: someDict.values()
# Hay un doble bucle... un follon que duplica los valores. Es más simple 

# for x in allGuests:
#     for k,v in allGuests[x].items():
#          print(allGuests[x].get('apples',0))


allGuests.get('Bob')
allGuests.get('Pedro','No existe')
allGuests.get('Carol','No existe')

allGuests.get('Carol','No existe').get('apples',0)

for v1 in allGuests.values():
    for k in v1:  #.items():
        print(k)



### A: Iterating the values view of the main dictionary

def countThings(glist,thing):
    count = 0
    for v in glist.values():
        count += v.get(thing,0)
    return count

print('Things Brought:')
print('---- Apples: ' + str(countThings(allGuests,'apples')))





### B: Iterating the keys in the main dictionary

def countThings2(glist,thing):
    count = 0
    for x in glist:
        count += glist[x].get(thing,0)
    return count

print('Things Brought:')
print('---- Apples: ' + str(countThings2(allGuests,'apples')))
            
            
        
    
# Creating a list with all the available key in the nested dictionaries


# To avoid having repeated keys I will use the setdefault method for dicitonaries


allThings = {}

def addThings(tlist):
    for v1 in allGuests.values():
        for k in v1:
            tlist.setdefault(k,0)

addThings(allThings)

list(allThings)


def addCount():
    for key in allThings:
        count = 0
        for v1 in allGuests.values():
            count += v1.get(key,0)
        allThings[key] = count
    return allThings



def addCount2(glist,tlist):
    for key in tlist:
        tlist[key] = countThings(glist,key)        
    return tlist


        
### Borrar valores de un diccionario

for k in allThings:
    allThings[k] = 0























































































