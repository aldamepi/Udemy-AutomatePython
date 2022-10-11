#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 23:17:14 2022

@author: albertomengual
"""

def w1():
    spam = 0
    
    while spam < 5:
        print ('Hello world!')
        spam += 1
    
def ifW():
    spam = 0
    
    if spam < 5:
        print ('Hello world!')
        spam += 1


def w2():
    name = ''
    
    while name != 'your name':
        name = input('Please type your name: ')
    print('Thank you!')


def wx(): # That's a bug
    while True:
        print('Hello!') # KeyboardInterrupt wiht ctrl+c


def w3():
    while True: #it will never be False
        name = input ('Please type your name: ')
        if name == 'your name':
            break # causes the execution to immediately jump out of this loop
    print('Thank you!')
        

def wC():
    spam = 0
    while spam < 5:
        spam += 1
        if spam == 3:
            continue # whem spam == 3 the next print function will never happen
        print('spam is ' + str(spam))
        

def wS():
    while True:
        name = input('Who are you? ')
        if name != 'Joe':
            continue
        print('Hello, Joe. What\'s the password? (fish) ')
        password = input()
        if password == 'swordfish':
            break
    print('Access granted.')


def wS2():
    name = ''
    password = ''
    
    while name != 'Joe':
        name = input('Who are you? ')
    print('Hello, Joe.')
    while password != 'swordfish':
        password = input('What\'s the password? (fish) ')        
    print('Access granted.')




