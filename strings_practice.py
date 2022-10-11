#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 20:43:31 2022

@author: albertomengual
"""


' STRINGS PRACTICE '.center(78,'#')
############################## STRINGS PRACTICE ##############################


def validateInput():
    while True:
        age = input('Enter you age: ')
        if age.isdecimal():
            break
        print('Please type numeric characters.', end = '')
    
    while True:
        password = input('Enter a new password (letters and numbers only):\n')
        if password.isalnum() and len(password) >= 8:
            break
        print('The password minimum length must be 8 characters: numbers \
or letters', end = '')


' PICNIC TABLE'.rjust(40,'#')
########################### PICNIC TABLE

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}

def printPicnicI (plist,lw,rw):
    print('PICNIC ITEMS'.center(lw+rw, '-'))
    
    for k,v in plist.items():
        print(k.ljust(lw, '.')+str(v).rjust(rw))

printPicnicI(picnicItems,20,6)







































































































