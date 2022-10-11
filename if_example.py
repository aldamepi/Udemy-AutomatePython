#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 15:23:19 2022

@author: albertomengual
"""
def if1():
    name = 'Alice'
    
    if name == 'Alice':
        print('Hi Alice')
    
    print('Done')



def if2():
    clave = 'swordfish'
    
    if clave == 'swordfish':
        print('Access Granted!')
    else:
        print('Wrong Password :(')
    
    
def ifelif():
    name = 'Bob'
    age = 3000
    
    if name == 'Alice':
        print('Hi Alice')    
    elif age < 12:
        print('You\'re not Alice, kiddo.')
    elif age > 2000:
        print('Unlike you, Alice is not an undead, immortal vampire.')
    elif age > 100:
        print('You are not Alice, grannie.')
    
    print('Done')
    
def truthy():
     name = input('Enter a name: ')
     # The name variable is set to anything the user types in. But input will
     # be returning a string value, not a boolean True or False value.
     # The conditions can use "truthy" or "falsey" values.
     if name: # Condition evaluates to the blank string "Falsey" value
         print('Thank you for entering a name.')
     else:
         print('You did not enter a name.')
         
def betterT():
     name = input('Enter a name: ')
   
     if name != '': # Condition evaluates to the blank string "Falsey" value
         print('Thank you for entering a name.')
     else:
         print('You did not enter a name.') 


def betterT2():
     name = input('Enter a name: ')
   
     if bool(name): # Condition evaluates to the blank string "Falsey" value
         print('Thank you for entering a name.')
     else:
         print('You did not enter a name.') 



         
         
         