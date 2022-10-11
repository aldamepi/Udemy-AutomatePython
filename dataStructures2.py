#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 20:07:25 2022

@author: albertomengual
"""
# DATA STRUCTURES PRACTICE 2



############# CHESS DICTIONARY VALIDATOR #######################

# The following dictionary represents a chess board

board = {'1h': 'bking', 
         '6c': 'wqueen', 
         '2g': 'bbishop', 
         '5h': 'bqueen', 
         '3e': 'wking'}


####### INSTRUCTIONS 
# The function isValidChessBoard() returns True or False depending on if the 
# board is valid.
# A valid board:
    # Will have exactly one black king and exactly one white king.
    # Each player can only have at most 16 pieces: at most 8 pawns...
    # All pieces must be on a valid space from '1a' to '8h' (i.e. not on '9z')
# The piece names begin with either 'w' or 'b'... followed by:
    # 'pawn'
    # 'knight'
    # 'bishop'
    # 'rook'
    # 'queen'
    # 'king'
# This function should detect when a bug has resulted in an improper 
# chees board
        




######## CODE

# I will divide the function isValidCheesBoard() in smaller functions that 
# that check the VALIDITY



# Check the kings
# count 'wking' and count 'bking' must be both 1

def checkKings(b):
    cwk = 0
    cbk = 0
    for v in b.values():
        if v == 'wking':
            cwk += 1
        if v == 'bking':
            cbk += 1
    if cwk == 1 and cbk == 1:
        return True
    else:
        print('Kings bug')
        return False


# Check Pawns

def checkPawns(b):
    cwp = 0
    cbp = 0
    for v in b.values():
        if v == 'wpawn':
            cwp += 1
        if v == 'bpawn':
            cbp += 1
    if cwp < 9 and cbp < 9:
        return True
    else:
        return False



# Check pieces
# The amount of pieces that begin with 'w' or 'b' must be <=16

def checkPieces(b):
    cw = 0
    cb = 0
    for v in b.values():
        if v[0] == 'w':
            cw += 1
        if v[0] == 'b':
            cb += 1
    if cw <= 16 and cb <= 16:
        return True
    else: 
        return False


# Check spaces
# I create a list with all the possible valid spaces and then check if the 
# keys of the board dictionary are on it.


## Create spaces list
letters = ['a','b','c','d','e','f','g','h']
numbers = list(range(1,9))

spaces = []

for n in numbers:    
    for l in letters:
        spaces.append(str(n)+l)


## Function
def checkSpaces(b):
    for k in b:
        if k not in spaces:
            return False
    return True


    
    

    

##### Create the definite function

def isValidChessBoard(b):
    if checkKings(b) and \
       checkPawns(b) and \
       checkPieces(b) and \
       checkSpaces(b):
           return True
    print('Bug detected: improper chess board')
    return False

# !!!! If a subfunction is changed the main function definition must be 
# executed too before calling it again.          


# Call the function

isValidChessBoard(board)



# Test code

# board['9j'] = 'wpawn' # check functions with two returns - checkSpaces
# del board['9j']

# board['2e'] = 'wking'
# del board['2e']





















































































