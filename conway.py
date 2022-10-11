#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 20:48:52 2022

@author: albertomengual
"""


# CONWAY'S GAME OF LIFE
# example of cellular automata: a set of rules governing the behavior of a field
# made up of discrete cells.




# RULES:
# A filled-in square will be "alive" and an empty square will be "dead"
# If a living square has two or three living neighbors, it continues to live 
# on the next step.
# If a dead square has exactly three living neighbors, it comes alive on the 
# next step.
# Every other square dies or remain dead on the next step.



# We can use a list of lists to represent th two-dimensional field.
# The inner list represents each column of squares and stores a '#' hash string
# for living squares and a ' ' space string for dead squares.
    

####### ORIGINAL CODE #############


# import random, time, copy




# WIDTH = 60
# HEIGHT = 20

# # Create a list of list for the cells:
# nextCells = []
# for x in range(WIDTH):
#     column = [] # Create a new column.
#     for y in range(HEIGHT):
#         if random.randint(0, 1) == 0:
#             column.append('#') # Add a living cell.
#         else:
#             column.append(' ') # Add a dead cell.
#     nextCells.append(column) # nextCells is a list of column lists.

# while True: # Main program loop.
#     print('\n\n\n\n\n') # Separate each step with newlines.
#     currentCells = copy.deepcopy(nextCells)

#     # Print currentCells on the screen:  ??? Is there no other way?
#     for y in range(HEIGHT):
#         for x in range(WIDTH):
#             print(currentCells[x][y], end='') # Print the # or space.
#         print() # Print a newline at the end of the row.

#     # Calculate the next step's cells based on current step's cells:
#     for x in range(WIDTH):
#         for y in range(HEIGHT):
#             # Get neighboring coordinates:
#             # `% WIDTH` ensures leftCoord is always between 0 and WIDTH - 1
#             leftCoord  = (x - 1) % WIDTH # ??? Check: for x in range(20): print((x-1)%20)
#             rightCoord = (x + 1) % WIDTH # matemáticas
#             aboveCoord = (y - 1) % HEIGHT
#             belowCoord = (y + 1) % HEIGHT

#             # Count number of living neighbors:
#             numNeighbors = 0
#             if currentCells[leftCoord][aboveCoord] == '#':
#                 numNeighbors += 1 # Top-left neighbor is alive.
#             if currentCells[x][aboveCoord] == '#':
#                 numNeighbors += 1 # Top neighbor is alive.
#             if currentCells[rightCoord][aboveCoord] == '#':
#                 numNeighbors += 1 # Top-right neighbor is alive.
#             if currentCells[leftCoord][y] == '#':
#                 numNeighbors += 1 # Left neighbor is alive.
#             if currentCells[rightCoord][y] == '#':
#                 numNeighbors += 1 # Right neighbor is alive.
#             if currentCells[leftCoord][belowCoord] == '#':
#                 numNeighbors += 1 # Bottom-left neighbor is alive.
#             if currentCells[x][belowCoord] == '#':
#                 numNeighbors += 1 # Bottom neighbor is alive.
#             if currentCells[rightCoord][belowCoord] == '#':
#                 numNeighbors += 1 # Bottom-right neighbor is alive.

#             # Set cell based on Conway's Game of Life rules:
#             if currentCells[x][y] == '#' and (numNeighbors == 2 or
# numNeighbors == 3):
#                 # Living cells with 2 or 3 neighbors stay alive:
#                 nextCells[x][y] = '#'
#             elif currentCells[x][y] == ' ' and numNeighbors == 3:
#                 # Dead cells with 3 neighbors become alive:
#                 nextCells[x][y] = '#'
#             else:
#                 # Everything else dies or stays dead:
#                 nextCells[x][y] = ' '
#     time.sleep(1) # Add a 1-second pause to reduce flickering.








######### Algoritmo ############


# Importar las librerias

# Crear la matriz inicial:
#     Crear una lista de listas
#     Crear un array de numpy
# Medidas ancho 60 alto 20

# (Muestra la matriz inicial) - se puede meter en el bucle

# Aqui se empieza un bucle que muestra la evolucion de la matriz

# Crar una copia de la matriz inicial

# Modificar la copia:
#     identificar las coordenadas de las posiciones adyacentes a cada cuadro
#     calcular las condiciones de cada cuadro en funcion de la posicion inicial
#     determinar la condicion futra de cada cuadro en la copia

# time.sleep - pausa
# Volver a print - s
    
    

import random, time, copy
import numpy as np



# Create de initial matrix

width = 60
height = 20




## With built-in and randint

printedMatrix = []

def createMatrix(matrix0):
    for i in range(height):
        row= []
        for j in range(width):
            if random.randint(0,1) == 0:
                row.append(' ')
            else:
                row.append('#')
        # print(row)
        matrix0.append(row)

createMatrix(printedMatrix)


## Option B: with numpy

# matrix0 = np.random.choice((' ','@'), size=(height,width))

# Print the elements of the matrix with a loop:
    
def printMatrix(matrix0):
    print('\n\n\n\n\n')    
    for i in range(height):
        for j in range(width):
            print(matrix0[i][j], end='')
        print()

# Calculate next step:
    
def nextStep(matrix0):
    for i in range(height):
        for j in range(width):
            
            
            # Define the coordinates
            
            leftCoord = (j-1)%width
            rightCoord = (j+1)%width
            aboveCoord = (i-1)%height
            belowCoord = (i+1)%height
            
                           
            # Count living neighbors  ??? Create a new loop
            
            livingC = 0
            
            if matrix1[aboveCoord][leftCoord] == '#':
                livingC += 1
            if matrix1[aboveCoord][j] == '#':
                livingC += 1
            if matrix1[aboveCoord][rightCoord] == '#':
                livingC += 1
            if matrix1[i][leftCoord] == '#':
                livingC += 1
            if matrix1[i][rightCoord] == '#':
                livingC += 1
            if matrix1[belowCoord][leftCoord] == '#':
                livingC += 1
            if matrix1[belowCoord][j] == '#':
                livingC += 1
            if matrix1[belowCoord][rightCoord] == '#':
                livingC += 1
            
            
            # Change each position in the matix displayed ??? Create a new loop?
            
            if matrix1[i][j] == '#' and (livingC == 2 or livingC == 3):
                matrix0[i][j] = '#'
            elif matrix1[i][j] == ' ' and livingC == 3:
                matrix0[i][j] = '#'
            else:
                matrix0[i][j] = ' '
                

# Create the loop of the game:
    
while True:
    
    # Print an interval of lines to separete each step:
    
    # print('\n\n\n\n\n')

    

    # Print the elements of the matrix with a loop:
    
    # def printMatrix(matrix0):    
    #     for i in range(height):
    #         for j in range(width):
    #             print(matrix0[i][j], end='')
    #         print()
    
    
    printMatrix(printedMatrix)
    
    
    
    # Copy the matrix0 to have a pattern to make the calculation with
    
    matrix1 = copy.deepcopy(printedMatrix)
    
    # matrix1 = printedMatrix.copy()
        
    
    # Calculate next step:
    
    # def nextStep(matrix0):
    #     for i in range(height):
    #         for j in range(width):
                
                
    #             # Define the coordinates
                
    #             leftCoord = (j-1)%width
    #             rightCoord = (j+1)%width
    #             aboveCoord = (i-1)%height
    #             belowCoord = (i+1)%height
                
                               
    #             # Count living neighbors  ??? Create a new loop
                
    #             livingC = 0
                
    #             if matrix1[aboveCoord][leftCoord] == '#':
    #                 livingC += 1
    #             if matrix1[aboveCoord][j] == '#':
    #                 livingC += 1
    #             if matrix1[aboveCoord][rightCoord] == '#':
    #                 livingC += 1
    #             if matrix1[i][leftCoord] == '#':
    #                 livingC += 1
    #             if matrix1[i][rightCoord] == '#':
    #                 livingC += 1
    #             if matrix1[belowCoord][leftCoord] == '#':
    #                 livingC += 1
    #             if matrix1[belowCoord][j] == '#':
    #                 livingC += 1
    #             if matrix1[belowCoord][rightCoord] == '#':
    #                 livingC += 1
                
                
    #             # Change each position in the matix displayed ??? Create a new loop?
                
    #             if matrix1[i][j] == '#' and (livingC == 2 or livingC == 3):
    #                 matrix0[i][j] = '#'
    #             elif matrix1[i][j] == ' ' and livingC == 3:
    #                 matrix0[i][j] = '#'
    #             else:
    #                 matrix0[i][j] = ' '
                    
            
    nextStep(printedMatrix)
    
    time.sleep(1)





























































