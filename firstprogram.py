#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 20:02:03 2022

@author: albertomengual
"""

# This program says hello and asks for my name
def saludo():
    print('Hello World!')
    
    myName = input('What\'s your name? ') # ask for their name
    print('\nIt\'s good to meet you ' + myName + '!')
    print()
    print('The length of your name is:')
    print(len(myName))
    
    print('What is your age?') # ask for their age
    age = input()
    age = int(age)
    print('\nYou will be ' + str(age + 1) + ' in a year.')
    
def saludo2():
    print('Hello World!')
    
    myName = input('What\'s your name? ') # ask for their name
    # print('\nIt\'s good to meet you ' + myName + '!')
    # print()
    # print('The length of your name is:')
    # print(len(myName))
    
    print('What is your age?') # ask for their age
    age = input()
    # age = int(age)
    print('Your name is {0} and your age is {1}.'.format(myName,age))




