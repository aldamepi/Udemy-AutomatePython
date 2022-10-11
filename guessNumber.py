#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 18:57:52 2022

@author: albertomengual
"""
# This is a guess the number game


import random

name = input('What\'s your name?!\n')

nSecret = random.randint(1,20)

print('Well ' + name + ', I am thinking of a number between 1 and 20.')

# ask the player to guess 6 times.
for i in range (1,7):
    print('Take a guess.')
    nGuess = int(input())
        #'Type an integer between 1 and 20: '))
    if nGuess > nSecret:
        print('Your guess is too high.')
    if nGuess < nSecret:
        print('Your guess is too low.')    
    if nGuess == nSecret: # this condition is the correct guess.
        # print('You are right ' + str(nSecret) + ' is the secret number.')
        # print('It tooked you ' + str(i) + ' guesses.')
        break

if nGuess == nSecret:
    print('Good job, ' + name + '! You guessed my number in ' + str(i) + ' guesses!')
else:
    print('Nope. The number I was thinking of was: ' + str(nSecret) + '.')
    
    









