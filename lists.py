#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 00:12:36 2022

@author: albertomengual


"""

import random
import copy




# recorrer una lista o cadena en sentido inverso

bacon = ''
for c in reversed(spam[0]):
    bacon += c
print(bacon)

bacon = ''
for c in spam[0]:
    bacon = c + bacon
print(bacon)

print(spam[0][::-1])




# Función crear lista 

def allMyCats():
    cats = []
    while True:
        name = input('Enter the name of the cat ' + str(len(cats) + 1) +
                     ' (or nothing to stop):\n')
        if name == '':
            print('That is all folks')
            break
        else:
            cats += [name] # ojo [] se trata de concatenar listas:
                           # cats = ['name1'] + ['name2'] = ['name1', 'name2']
    print('The name of the cats are: ')
    for n in cats:
        print(' ' + n)
        


# Concatenar listas y strings

eggs = []

eggs = 'Hello'

eggs += ' world'



# Check items in a list

def myPets():
    mypets = ['arturito', 'pablito', 'karspersky']
    while True:
        pName = input('Enter the name of the pet (press enter to exit): \n')
        if pName == '':
            break
        elif pName in mypets:
            print('I have a pet called ' + pName + '.')
        else:
            print('I do not have any pet named that way.')



# for loops with lists

for i in range(len(spam)):
    print('Index ' + str(i) + ' in spam is: ' + spam[i])



saussage = []

for i in range(4):
    saussage += [i]

saussage = list(range(4))





saussage = list(str(2351))
saussage = list(map(int,saussage)) ## ejemplo de map!!!!
saussage = list(map(int,str(2351)))

saussage = list(map(list,saussage)) ## TypeError
saussage = list(map(tuple,saussage)) ## TypeError

saussage = list(map(tuple,str(2351)))




# Augmented assignment operators

bacon = 47

bacon / 7

bacon % 7

bacon = bacon % 7

bacon






# ¿Qué es una lista intensiva o por comprensión?

# Crea una lista a partir de un iterable, se le puede pasar una expresión 
# a cada elemento y una condicion al iterable. Será o no in place según
# la expresión.

[x * 2 for x in spam if 'i' in x] # [expresión for item in iterable if condición]

[spam.remove(x) for x in spam if 'o' in x] # sigue borrando solo la primera 
                                           # coincidencia, in place

[sorted(x) for x in spam2 if 'a' in x]

[spam.sort(reverse=True) for x in spam2 if 'e' in x] # esto no tiene sentido
# ordena una lista en función de si otra lista distinta cumple una condición...





def magic8B():
    answers = ['It is certain',
               'It is decidedly so',
               'Yes',
               'Reply hazy try again',
               'Ask again later',
               'Concentrate and ask again',
               'My reply is no',
               'Outlook not so good',
               'Very doubtful']
    n = random.randint(0,len(answers)-1)
    print(answers[n])

    

c = 8


def scope(i):
    return i * 3


 

# references, id and copy

cheese = copy.copy(spam2)
cheese = copy.copy(saussage)
cheese.index('spam')
cheese[8][0]='bacon'
cheese = copy.deepcopy(saussage)










































