#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 11:53:10 2022

@author: albertomengual
"""


def f1():
    print('My name is')
    
    for i in range(5):
        print('Jimmy Five Times ' + str(i))
    # The code in the for loop is run five times. The first time it is run, the 
    # variable i is set to 0. After the for clause execution, it goes back to the 
    # top of the loop, and the for statement increments i by one.
    # The variable i will go up to (but will not include) the integr passed to 
    # range().
    


def fG(): # Gauss: Una función que suma los numeros del 1 al 100
    total = 0 
    for i in range(101):
        total += i
    print(total)

sum(range(101))


def wF(): # An equivalent to the f1() with a while loop
    print('My name is')
    i = 0
    while i < 5:
        print('Jimmy Five Times ' + str(i))
        i += 1
        



