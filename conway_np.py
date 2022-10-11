#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 21:15:45 2022

@author: albertomengual
"""

import numpy as np
import sys


np.set_printoptions(threshold=sys.maxsize)

# np.random.random((20,60))
# np.empty((20,60))
# np.ones((20,60))


# Crear matriz aleatoria con ' ' y '#'

width = 60
height = 20

matrix = np.random.choice(a=[' ','#'], size = (height,width))
print(matrix, sep='')
print(matrix.tolist())

matrix2 = matrix # las matrices son mutables
print(id(matrix))
id(matrix2)


lst = []

for x in matrix:
    lst.append(x)
    
matrix[1]
print(matrix[0][0])
print(matrix[0][:],sep='')


for x in range(width):
    lst.append(matrix[0][x])
    


for y in range(height):
        for x in range(width):
            print(matrix[y][x], end='') # Print the # or space.
        print() 











































