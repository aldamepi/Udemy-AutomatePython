#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 19:44:22 2022

@author: albertomengual
"""

# This is a rock, paper, siccors game


# import random, sys

# print('ROCK, PAPER, SCISSORS')

# # These variables keep track of the number of wins, losses, and ties.
# wins = 0
# losses = 0
# ties = 0

# while True: # The main game loop.
#     print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
#     while True: # The player input loop. This loop validates the input.
#         print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
#         playerMove = input()
#         if playerMove == 'q':
#             print('Goodbye.')
#             sys.exit() # Quit the program.
#         if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
#             break # Break out of the player input loop.
#         print('Type one of r, p, s, or q.') # Another way appart from elif and else

#     # Display what the player chose:
#     if playerMove == 'r':
#         print('ROCK versus...')
#     elif playerMove == 'p':
#         print('PAPER versus...')
#     elif playerMove == 's':
#         print('SCISSORS versus...')

#     # Display what the computer chose:
#     randomNumber = random.randint(1, 3)
#     if randomNumber == 1:
#         computerMove = 'r'
#         print('ROCK')
#     elif randomNumber == 2:
#         computerMove = 'p'
#         print('PAPER')
#     elif randomNumber == 3:
#         computerMove = 's'
#         print('SCISSORS')

#     # Display and record the win/loss/tie:
#     if playerMove == computerMove:
#         print('It is a tie!')
#         ties = ties + 1
#     elif playerMove == 'r' and computerMove == 's':
#         print('You win!')
#         wins = wins + 1
#     elif playerMove == 'p' and computerMove == 'r':
#         print('You win!')
#         wins = wins + 1
#     elif playerMove == 's' and computerMove == 'p':
#         print('You win!')
#         wins = wins + 1
#     elif playerMove == 'r' and computerMove == 'p':
#         print('You lose!')
#         losses = losses + 1
#     elif playerMove == 'p' and computerMove == 's':
#         print('You lose!')
#         losses = losses + 1
#     elif playerMove == 's' and computerMove == 'r':
#         print('You lose!')
#         losses = losses + 1













## EN ESPAÑOL DESDE CERO



import random, sys

print ('PIEDRA, PAPEL O TIJERAS')


# Definir las variables del marcador

victoria = 0
empate = 0
derrota = 0

while True:
    print('%s Victorias, %s Empates, %s Derrotas' % (victoria,empate,derrota))
    
    # Bucle de validación del input o salida
    while True:
        print ('¿Qué elijes?: (p)iedra, p(a)pel, (t)ijeras o (s)alir')
        jugada = input()
        if jugada == 's':
            print('Adioos')
            sys.exit()
        elif jugada == 'p' or jugada == 'a' or jugada == 't':
            print('Has elegido:')
            break
        else:
            print('Introduce p, a, t o s.')
    
    # Mostrar la jugada elegida
    if jugada == 'p':
        print('PIEDRA contra...')
    elif jugada == 'a':
        print('PAPEL contra...')
    elif jugada == 't':
        print('TIJERAS contra...')
    
    # Mostrar la jugada del ordenador
    n = random.randint(1,3)
    if n == 1:
        jugCompu = 'p'
        print('PIEDRA')
    elif n == 2:
        jugCompu = 'a'
        print('PAPEL')
    elif n == 3:
        jugCompu = 't'
        print('TIJERAS')
    
    # Calcular el resultado de la partida
    if jugada == jugCompu:
        print('Empate :|')
        empate += 1
    elif jugada == 'p' and jugCompu == 't':
        print('Prieda rompe tijeras: Ganas!')
        victoria +=1
    elif jugada == 't' and jugCompu == 'a':
        print('Tijera corta papel: Ganas!')
        victoria +=1
    elif jugada == 'a' and jugCompu == 'p':
        print('Papel envuelve a la piedra: Ganas!')
        victoria +=1
    elif jugada == 't' and jugCompu == 'p':
        print('Prieda rompe tijeras: Pierdes!')
        derrota +=1
    elif jugada == 'a' and jugCompu == 't':
        print('Tijera corta papel: Pierdes!')
        derrota +=1
    elif jugada == 'p' and jugCompu == 'a':
        print('Papel envuelve a la piedra: Pierdes!')
        derrota +=1
        
        

def practice():
    spam = input('1, 2 or anything else: ')
    if spam == '1':
        print('Hello')
    elif spam == '2':
        print('Howdy')
    else:
        print('Greetings!')


def p():
    for i in range(1,11):
        print(i, end = ', ')
        
def p2():
    i = 1
    while i <= 10:
        print(i)
        i += 1












































































