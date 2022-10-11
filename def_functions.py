#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 19:34:42 2022

@author: albertomengual
"""


def hello():
    print('Howdy!')
    print('Howdy!!!!')
    print('Hello There.')

hello()
hello()
hello()



def hi2(name): # the parameter is the variable that have arguments assigned
    print('Hello ' + name)


hi2('Juanita') # the argument is the value passed in the function call 
hi2('Albertito')



def plusOne (number):
    return number + 1


newNumber = plusOne(5)
print(newNumber)






import random

def getAnswer(answerNumber):
    if answerNumber == 1:
           return 'It is certain'
    elif answerNumber == 2:
           return 'It is decidedly so'
    elif answerNumber == 3:
           return 'Yes'
    elif answerNumber == 4:
           return 'Reply hazy try again'
    elif answerNumber == 5:
           return 'Ask again later'
    elif answerNumber == 6:
           return 'Concentrate and ask again'
    elif answerNumber == 7:
           return 'My reply is no'
    elif answerNumber == 8:
           return 'Outlook not so good'
    elif answerNumber == 9:
           return 'Very doubtful'

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)



print('Hello', end='')
print('World')


print('cat','dog','mouse', sep=', ')





