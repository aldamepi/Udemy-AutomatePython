#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 22:14:41 2022

@author: albertomengual

This script will get the text from the clipboard, add a star and space to 
the beiginning of each line, and then paste this new text to the clipboard

"""


import pyperclip as ppc


text = ppc.paste()



### Algorithm A
# split the lines of the text into a new list
# add '* ' at the beginning of each items
# rejoin the items of the list into a string with newlines '\n'
# upload to the clipboard





# Split the lines

splittedText = text.splitlines()



# Add '* ' to the beginning of each item in the list


# for i in splittedText:
#     i = '* ' + i
#     print(i) # !!! la variable i se destruye al finalizar el bucle


for i,v in enumerate(splittedText):
    splittedText[i] = '* ' + v # la lista permanece al terminar el bucle
   



# Rejoin the text

bulletedText = '\n'.join(splittedText)



# Copy to clipboard



ppc.copy(bulletedText)



# RESULT
# * Lists of animals
# * Lists of aquarium life
# * Lists of biologists by author abbreviation
# * Lists of cultivars




































































































