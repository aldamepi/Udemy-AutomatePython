#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 14:40:41 2022

@author: albertomengual
"""

import numpy as np


########### CHARACTER PICTURE GRID #############


# Input

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]



# Wanted output

# ..OO.OO..
# .OOOOOOO.
# .OOOOOOO.
# ..OOOOO..
# ...OOO...
# ....O....



# Sequence and loops tests

print(grid[-1][0], end='')
print(grid[-2][0], end='')
print(grid[-3][0], end='')
print(grid[-4][0], end='')


## It consists of a double loop alternating reverse and straight sequences.
## It is also necessary to obtain the length of the list and sublists.


# Alternative A: Using the lengths in range() functions

lSubL = len(grid[0])
lL = len(grid)


for j in range(lSubL):
    for i in range(lL-1,-1,-1):
        print(grid[i][j], end='')
    print()
 
    

# Alternative B: Try using reverse functions

for j in range(lSubL):
    for i in reversed(range(lL)):
        print(grid[i][j], end='')
    print()



# Alternative C: Try using enumerate 
### No compensa por la transposicion de indices. Probar en numpy

## Test enumerate

list(enumerate(grid))
list(enumerate(grid[0]))



for i,x in enumerate(grid[0]):
    print(x, end='')


for j,y in enumerate(grid):
    for i,x in enumerate(grid[j]):
        print(x, end='')
    print()

for j,y in enumerate(grid):
    for i,x in enumerate(grid[j]): 
#######  TypeError: 'enumerate' object is not reversible  #####
        print(y, end='')
    print()



# Alternative D: try with numpy


g = np.array(grid)

g = np.transpose(g)

g.shape[1]

list(g)
print(g)


for i in range(g.shape[0]):
    for j in range(g.shape[1]):
        print(g[i][j], end='')
    print()




# Alternative E: numpy enumerate


for i in range(g.shape[0]):
    for j,x in enumerate(g[i]):
        print(x, end='')
    print()













































































