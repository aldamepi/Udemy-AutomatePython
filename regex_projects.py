#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 00:50:38 2022

@author: albertomengual



"""

import re




########## DATE DETECTION
# Write a regex that can detect dates in the DD/MM/YYYY format

dateRE = re.compile(r'''(
    (0[1-9]|[1-2][0-9]|3[01])/
    (0[1-9]|1[0-2])/
    ([1-2][0-9]{3})
    )''', re.X)


# dateRE.search('25/02/2002')
# dateRE.search('31/02/2002')


# dateRE.search('35/32/3002')
# dateRE.search('35/02/2002')

while True: # input validation
    fecha = input('Enter a date in format DD/MM/YYYY: ')
    #date = input('Enter a date in format DD/MM/YYYY: ')
    
    try:
        day, month, year = dateRE.search(fecha).group(2,3,4)
        break
    except:
        print('Type a valid format date DD/MM/YYYY')

# Detect valid date

shortMonth = ['04','06','09','11']
longMonth = ['01','03','05','07','08','10','12']


def leapYear(yy):
    if yy%100 == 0 and yy%400 == 0:
        return True
    elif yy%100 == 0:
        return False
    elif yy%4 == 0:
        return True
    else:
        return False
    



if month in shortMonth and int(day) <= 30:
    print('Valid date')
elif month in longMonth and int(day) <= 31:
    print('Valid date')
elif leapYear(int(year)) and month == '02' and int(day) <= 29:
    print('Valid date')
elif not leapYear(int(year)) and month == '02' and int(day) <= 28:
    print('Valid date')
else:
    print('Invalid date')






############# STRONG PASSWORD DETECTION

# A strong password is defined as:
    # at least 8 characters long
    # contains both uppercase and lowercase
    # has at least one digit
    
password = ''

password = input('Enter a strong password: ')


p8cRE = re.compile(r'[ -/\w]{8,}')
pUlRE = re.compile(r'([a-z]{1}.*[A-Z]{1})|([A-Z]{1}.*[a-z]{1})')
pDRE = re.compile(r'\d')


def strongPass(ps):
    if p8cRE.search(ps) and pUlRE.search(ps) and pDRE.search(ps):
        print('Your password is strong')
        return True
    else:
        print('Please type a strong password')
        return False

# &Sx%erf1
# FsW^JV$H
# f*JROC0%3w

# BafDA7JlBT
# QoWfgI9A

# $fxgtlh*a^
# cNGZV21

strongPass('BafDA7JlBT')
strongPass('QoWfgI9A')
strongPass('$fxgtlh*a^')
strongPass('cNGZV21')
strongPass('&Sx%erf1')
strongPass('FsW^J4V$H') # No la identifica como segura







############# REGEX VERSION OF STRIP()

# A function that takes a string and does the same as the strip() method.
# Arguments: string and strip character
# If no second argument then strip whitespace characters from the beginning and
# end of the string, otherwise the characters specified in the second arguments 
# will be removed.

## TIP: Use sub() (ver CODE2)

### ALGORITHMN

# input the string

# define the function:
    # define the arguments of the function: string and character
    # create a regex that matches the stipping character at the beginning and end
    # clear the original string
    # return the resulting string 

# pass the function to the input string



########### CODE

# Libraries

# import re




# input

string0 = '   me encanta el carnaval   '
string0 = 'hhhme encanta el carnavaldddd'
# string0 = input('Enter the string to be stripped: ')

characStripped = input('Enter the characters to be stripped (or intro for None): ')


# define the function

# def stripRegex(st,chSt):
    
#     if chSt == None or chSt == '':
#         chSt = ' '
    
#     stripRE = re.compile(r'^[%s]*((\s?\w+)+)[%s]*$' %(chSt,chSt))
    
#     mo = stripRE.search(st)
    
#     return mo.group(1)




# # TEST CODE

# stripRegex(string0,None)
# stripRegex(string0,'hd')


# chSt = 'hd'

# stripRE = re.compile(r'^[%s]*((\s?\w+[^%s]*)+)[%s]*$' %(chSt,chSt,chSt))
# #stripRE = re.compile('^([{0}])(.*)([{0}])$'.format(chSt))    
# #stripRE = re.compile('^([%s])(\w+.*\w+)+([%s])$' %(chSt,chSt))


# mo = stripRE.search(string0)
# stripRE.findall(string0)

# mo.groups()
# mo.group(1)



# # frase sin espacios

# frase = 'me encanta el carnaval'

# fraseRE = re.compile(r'((\w+\s*)+)')

# mo = fraseRE.search(frase)

# mo.groups()





########### CODE2

def stripRX2(st,ch=' '):
    stRE2 = re.compile(f'^[{ch}]*|[{ch}]*$')
    string1 = stRE2.sub('',st)
    return string1


stripRX2(string0)
stripRX2(string0,'hd')







# Test Code

stRE2 = re.compile(f'^[ ]*|[ ]*$')

stRE2 = re.compile(f'^[hd]*|[hd]*$')

mo2 = stRE2.search(string0)
stRE2.findall(string0)

mo2.groups()
mo2.group()



























































