#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 16:59:51 2022

@author: albertomengual
"""


import pprint



# PRACTICE DICTIONARIES 1


# Write a program to return the birthday date of people stored in a dictionary
# Ask the user the name
# Return the value
# If the name doesn't exist ask to intoduce the date






def birthdays():
    global birthdays
    birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
    
    while True:
        name = input('Enter a name (blank to quit): ')
        if name == '':
            print('Good bye')
            break
        elif name in birthdays: # checking keys
            print('Birthday: ' + birthdays[name])
        else:
            print(name + '\'s birthday is not registered.')
            bd = input('Enter the birthday of ' + name + ':')
            birthdays[name] = bd
            print('Birthday database updated.')
        




birthdays

list(birthdays) # it will show the keys


# keys, values and items methods
# return view objects # len, iter, in reversed

for v in myCat.values():
    print(v)
    
for k in myCat: # == myCat.keys()
    print(k)

for i in myCat.items():
    print(i)

for k,v in myCat.items():
    print('Key: ' + k + '. Value: ' + v + '.')





# get() method

myCat.get('weight',0) # If the key does not exist, then return the second argument


# setdefault() method

spam = {}

spam.setdefault('c1') # Introduces None to the unexisting key

spam.setdefault('c1',0) # As the key already exists it will not change the value

spam.setdefault('c2',[])
spam['c2'] += ['cheese']
spam['c2'] += ['bacon']

## Practice setdefault()

## Short program that counts the number of occurences of each letter in a string.


def charCount():
    message = 'It was a bright cold day in April, and the clocks were striking \
         thirteen'
    
    count = {}
    
    for c in message:
        count.setdefault(c,0)
        count[c] += 1
    return count


def charCount2():
    message = 'It was a bright cold day in April, and the clocks were striking \
         thirteen'
    
    count = {}
    
    for c in message.upper():
        count.setdefault(c,0)
        count[c] += 1
    print(count)
    return count


def prettyCharCount():
    message = 'It was a bright cold day in April, and the clocks were striking \
         thirteen'
    
    count = {}
    
    for c in message.upper():
        count.setdefault(c,0)
        count[c] += 1
    pprint.pprint(count)
    return pprint.pformat(count)




# Dictionaries Comprehension

dc = {x: x ** 2 for x in range(5)}

dc2 = {k: v *2 for k,v in myCat.items()}






len(spam) # n items

del dc[3] # deletes the key (item)

iter(dc) # returns iterator through the keys of the dictionary

clear() # deletes the contents of a dictionary

spam2 = spam.copy() # creates a copy of the dictionary itself with different ids
                    # nested list and nested dictionaries??? -> references
id(spam)
id(spam2)


pop()

popitem()

reversed() # returns a reversed iterator

update(otherDict) # updates the dictionary using another one











































































