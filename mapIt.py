#! /Users/albertomengual/opt/anaconda3/bin/python
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 15:48:11 2022

@author: albertomengual

mapIt.py

Automatically launch the map in your browser using the contents of your
clipboard (or command line?).

What the program does:
    1. Gets a street address from the clipboard (or command line?)
    2. Opens the web browser to Google Maps page for the address


ALGORITHMN
1. Read the command line arguments? from sys.argv
2. Read the clipboard contents.
3. Call the webbrowser.open() funtion to open google maps


"""

# Import libraries

import sys, logging
import pyperclip as ppc
import webbrowser as wb

# print(logging.__file__)

# Configure Logging
logging.basicConfig(level=logging.DEBUG, 
                    format=' %(asctime)s -  %(levelname)s -  %(message)s')


logging.disable(logging.CRITICAL)


# Standard URL
"""
https://www.google.com/maps/place/Posada+del+Potro,+C.+Lucano,+17,+14003+Córdoba/
"""


logging.debug('Start of program')


# Handle the Command line Arguments
"""
The sys.argv variable stores a list of the program’s filename and command line 
arguments. If this list has more than just the filename in it, then len(sys.argv)
evaluates to an integer greater than 1, meaning that command line arguments have 
indeed been provided. sys.argv is a list of strings.
"""

# Check if command line arguments were passed
if len(sys.argv) > 1:
    # Get address from command line
    address = ' '.join(sys.argv[1:])
    logging.debug('Address obtained from command line: %s' %(address))

else:
    # Get address from clipboard
    address = ppc.paste()
    address = address.lower()
    address = address.replace('/',' ')
    address = address.replace('planta','')
    logging.debug('Address obtained from clipboard: %s' %(address))


# Launch the browser

wb.open('https://www.google.com/maps/place/' + address)


logging.debug('End of program')





















































































