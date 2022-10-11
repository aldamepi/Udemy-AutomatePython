#! /Users/albertomengual/opt/anaconda3/bin/python

# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python3

Created on Tue Mar  8 22:33:35 2022

@author: albertomengual

DEBUGGING

LOGGING

"""


import logging


# logging.basicConfig(level=logging.DEBUG, 
#                     format=' %(asctime)s -  %(levelname)s -  %(message)s')

# open('myProgramLog.txt', 'w')

logging.basicConfig(filename='myProgramLog.txt', 
                    level=logging.DEBUG, 
                    format='%(asctime)s -  %(levelname)s -  %(message)s')

#logging.disable(logging.CRITICAL)

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s%%)'  % (n))
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)'  % (n))
    return total

print(factorial(5))
logging.debug('End of program')

# open('myProgramLog.txt', 'w').close()





























































































