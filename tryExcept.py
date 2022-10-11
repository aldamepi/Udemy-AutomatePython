#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 13:53:10 2022

@author: albertomengual
"""

# import sys

def div42by(divB):
    return 42 / divB


def testDiv():
    print(div42by(2)) # without print() the returned value would not be  
                      # displayed in the shell
    print(div42by(12))
    print(div42by(0))
    print(div42by(1))


def divTry42by(divB):
    try:
        return 42 / divB
    except ZeroDivisionError:
        print ('Error: Your tried to divide by zero.')



def testDiv2():
    print(divTry42by(2))
    print(divTry42by(12))
    print(divTry42by(0)) # it will print the absence of value returned by
                         # the except print(): None
    print(divTry42by(1))

print(print(42))
# spam = []
# spam.append(testDiv2())


def testDiv3():
    global spamR
    spamR = []
    spamR.append(divTry42by(2))
    spamR.append(divTry42by(12))
    spamR.append(divTry42by(0)) # Call Stack: 
                                # divTry42by(0)
                                # error
                                # except print
                                # append returned value of the except print: None
    spamR.append(divTry42by(1))



def testDiv4():
    global spamP
    spamP = []
    spamP.append(print(divTry42by(2)))
    spamP.append(print(divTry42by(12)))
    spamP.append(print(divTry42by(0)))  # Call Stack: 
                                        # divTry42by(0)
                                        # error
                                        # except print
                                        # print return of the except print: None
                                        # append the returned value of 
                                        #   print(divT())
    
    spamP.append(print(divTry42by(1)))




def dT42T(divB):
    try:
        return 42 / divB
    except ZeroDivisionError:
        return 42 * 4


def test5():
    print(dT42T(2))
    print(dT42T(12))
    print(dT42T(0)) 
    print(dT42T(1))


def test6():
    global spam
    spam = []
    spam.append(dT42T(2))
    spam.append(dT42T(12))
    spam.append(dT42T(0))   # Call Stack: 
                            # divTry42by(0)
                            # error
                            # except return
                            # append returned value of except 
    spam.append(dT42T(1))


print(print(42))





def cats():
    print('How many cats do you have?')
    nCats = input()
    try:
        if int(nCats) >= 4:
            print('That\'s a lot of cats.')
        elif int(nCats) <= 0:
            print('Error: You do not have any cat at all or you borrowed them.')
        else:
            print('That is not that many cats.')
    except ValueError:
        print('You did not type a number.')



def cats2():
    #print('How many cats do you have?')
    nCats = None
    while type(nCats) is not int:
        try:
            nCats = int(input('How many cats do you have?\n'))
        except ValueError:
            print('You did not type a number.')
            # nCats = int(input('Please, type a number: '))
    # si la ejecución continua sin un valor para nCats, producirá otro error.
    if nCats >= 4:
        print('That\'s a lot of cats.')
    elif nCats <= 0:
        print('Error: You do not have any cat at all or you got rid of them.')
    else:
        print('That is not that many cats.')





def cats3():
    #print('How many cats do you have?')
    nCats = None
    while type(nCats) is not int or nCats <= 0:
        try:
            nCats = int(input('How many cats do you have?\n'))
            if nCats <= 0:
                print('Did you really get rid of your cats?')
                continue
        except ValueError:
            print('You did not type a number.')
        
    if nCats >= 4:
        print('That\'s a lot of cats.')
    # elif nCats <= 0:
    #     print('Error: You do not have any cat at all or you got rid of them.')
    else:
        print('That is not that many cats.')







def zigzag(): # exercise from the online book
    import time
    
    indent = 0
    indentIncreasing = True # the direction of the indentation increse
    
    try:
        while True: # Infinite loop
            print(' ' * indent, end = '')
            print('********')
            time.sleep(0.05) # Pause
            
            if indentIncreasing:
                indent += 1
                if indent == 20:
                    indentIncreasing = False
            else:
                indent -= 1
                if indent == 0:
                    indentIncreasing = True
    except KeyboardInterrupt:
        print('Goodbye, come back soon.')
                





# PRACTICE PROJECT COLLATZ 
# THE SIMPLEST IMPOSSIBLE MATH PROBLEM

def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1


def cs():
    print('Type an integer:')
    try:
        spam = int(input())
        while spam != 1:
            spam = collatz(spam)
    except:
        print('You did not type an integer.')
        
    
        
    























































