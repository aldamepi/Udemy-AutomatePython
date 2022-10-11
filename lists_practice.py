#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 23:21:59 2022

@author: albertomengual
"""

# LISTS PRACTICE PROJECTS


# COMMA CODE PRACTICE


## Testing lists

spam = ['apples','bananas','tofu','cats']

spam2 = []

spam3 = [4,7,23]



## Defining the function

def commaCode(someList):
    bacon = ''
    try:
        for i in range(len(someList)-1):
            bacon += str(someList[i]) + ', '
        bacon += 'and ' + str(someList[-1])
        return bacon
    except IndexError:
        print('Error: You introduced an empty list.')



## Testing calls

commaCode(spam)

commaCode(spam2)






# COIN FLIP STREAKS PRACTICE

import random

coin = ['H','T']
nFlips = 100

streakL = 6

nExperiments = 10000

flipList = []
nStreaks = 0

streakH = ['H']*streakL 
streakT = ['T']*streakL


def flips(sl):
    # sl = [] ### Si la creo localmente se destruye al finalizar la función
    for x in range(nFlips):
        sl += [random.choice(coin)]


def streak6(sl,s):
    global nStreaks, streakH, streakT
    
    # print(streakH)
    # print(streakT)
    # print(sl)
    for i in range(nFlips-s+1):
        # print(sl[i:i+s])
        if sl[i:i+s] == streakH or sl[i:i+s] == streakT:
            nStreaks += 1
    # return nStreaks





for e in range(nExperiments): 
    flipList = []
    flips(flipList)
    streak6(flipList,streakL)
# nStreaks = nStreaks * nExperiments


# what percentage of the coin flips contains a streak of six in a row.
# ????
print('Chance of streak: %s %%' % (nStreaks / 100))


























































