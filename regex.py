#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 18:21:47 2022

@author: albertomengual

Studying the Chapter 7: Regular Expressions

"""


import re


message = 'Call me 415-555-1011 tomorrow, or at 415-555-9998 is my office'

message2 = 'Call me 555-1011 tomorrow, or at (415)-555-9998 is my office'





# re.compile()

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

pNRegexP = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

pNR2 = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')


pNREo = re.compile(r'(\(\d\d\d\))?-(\d\d\d-\d\d\d\d)')




# re.search
matchObject = phoneNumRegex.search(message)

mop = pNRegexP.search(message)

mop2 = pNR2.search(message2)

moOp = pNREo.search(message2)


# match.group()

matchObject.group()
print(matchObject.group())


if matchObject: # Match objects have always True or None
    print(matchObject.group())

print(mop2.group(1))
mop2.groups()

moOp.group()
moOp.groups()


# re.findall() # returns a list of strings, it can be printed

phoneNumRegex.findall(message)
print(phoneNumRegex.findall(message))





# pattern.match() returns match object if match at the beginning

beginRegex = re.compile('Call me')
mo = beginRegex.match(message)
mo.group()




# match.groups() # Returns all of subgroups
# Useful with multiple assignment trick

areaCode, mainNumber = mop.groups()

areaCode, mainNumber = mop.group(1,2)





# The sub() method
re.sub(r'alber.*', 'yo', 'Me llamo alberto sin apellido', re.I)
subRE = re.compile(r'alber.*',re.I)
subRE.sub('yo','Me llamo Albertito sin apellido')


nameRE = re.compile(r'Agent \w+',re.I)
nameRE.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')

naGRE = re.compile(r'Agent (\w)\w*')
naGRE.sub(r'Agent \1****', 'Agent Alice Martinez told Agent Carol Lopez \
that Agent Eve Flores knew Agent Bob Sanchez was double agent.')






# Pipes |

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')

moPipe = batRegex.search('Batmobile lost a wheel')

moPipe.group()
moPipe.group(1)



# Optional Matching ? Zero or One

batRE = re.compile(r'Bat(wo)?man') # == 'Batman|Batwoman'

mo1 = batRE.search('The Adventures of Batman')

mo1.group()

mo2 = batRE.search('The Adventrues of Batwoman')

mo2.group()




# Match zero or more with the star *

batREmore = re.compile(r'Bat(wo)*man')

moMore = batREmore.search('The Adventures of Batwowowowoman')

moMore.group()
moMore.groups()





# Match one or more whit plus +

batREplus = re.compile(r'Bat(wo)+man')







# Match specific repetitions with braces {}

haRegex = re.compile(r'(Ha){3}')

haRegex.search('He said "HaHaHa"')

#haRegex.search('He said "HaHa"')


haRegex2 = re.compile(r'(Ha){3,5}')

haRegex2.search('He said "HaHaHaHa"') 



digitRE = re.compile(r'(\d){3,5}')
digitRE.search('1234567890')




# Findall again tuples
# Trick: to get the whole match above all the groups, create a group that
# contains all the other groups(()()())
movilRE = re.compile(r'''(
    (\+34|0034)?\s?    # prefijo españa
    (\d{3}[.-/\s]?\d{3}[.-/\s]?\d{3}) # telefono separado de 3 en 3
    |(\d{3}[.-/\s]?\d{2}[.-/\s]?\d{2}[.-/\s]?\d{2}) # telefono 3+2+2+2
    )''', re.X)

movilRE.findall("""Mis números de telefono son: \
               +34690915711 
               0034 606406801
               957.496803
               957/23/84/36
               606 40 68 03""")






# The caret and the dollar






# Matching everything wti the dot-star

dsRE = re.compile(r'First Name: (.*) Last Name: (.*)')
dsRE.search('First Name: Alberto Last Name: Mengual').groups()
dsRE.findall('First Name: Alberto Last Name: Mengual')


# Greedy non-greedy dot-star
ngRE = re.compile(r'<.*?>')
mo = ngRE.search('<To serve man> for dinner.>')
mo.group()

gRE = re.compile(r'<.*>')
mo = gRE.search('<To serve man> for dinner.>')
mo.group()




############ re.compile() expression's flags values

# Matching new lines with the DOT: re.S, re.DOTALL

prime = 'Serve the public trust.\nProtect the innocent.\nUpload the law.'
print(prime)
dsRE2 = re.compile(r'.*')
dsRE2 = re.compile(r'.*', re.DOTALL)
dsRE2 = re.compile(r'.*', re.S)
dsRE2.search(prime).group()



# Case-insensitive matching: re.I, re.IGNORECASE

robocopRE = re.compile(r'robocop', re.I)
robocopRE.search('ROBOCOP protects the innocent')


robocopRE2 = re.compile(r'.* robocop .*', re.I)
robocopRE2.search('Write a first line\nROBOCOP protects the innocent') == None


robocopRE2 = re.compile(r'.*robocop.*', re.I|re.S)
robocopRE2.search('Write a first line\nROBOCOP protects the innocent')




re.A
re.ASCII
# Make \w \W \b \B... perform ASCII-only matching instead of full Unicode
# matching






re.DEBUG
# Display debug information about compiled expressions




re.L
re.LOCALE
# Make ... dependent on the current locale.



re.M
re.MULTILINE 
# The pattern character '^' matches at the beginning of the string and at the 
# beginning of each line
# The pattern character '$' matches at the end of the string and at the end
# of each line.





re.X
re.VERBOSE
# Allows you to write regular expressions that look nicer 
# White space between the pattern is ignored, except when in character class
# can write comments wtih #

movilRE = re.compile(r'''(
    (\+34|0034)?\s?    # prefijo españa
    (\d{3}[.-/\s]?\d{3}[.-/\s]?\d{3}) # telefono separado de 3 en 3
    |(\d{3}[.-/\s]?\d{2}[.-/\s]?\d{2}[.-/\s]?\d{2}) # telefono 3+2+2+2
    )''', re.X)

movilRE.findall("""Mis números de telefono son: \
               +34690915711 
               0034 606406801
               957.496803
               957/23/84/36
               606 40 68 03""")





########### PRACTICE



# 20

commaNRE = re.compile(r'''(
    (\d{,3})
    (\d{1,3}(,\d{3})+)
    )''', re.X)


commaNRE = re.compile(r'((\d{1,3},)*\d{,3})')

commaNRE = re.compile(r'^\d{1,3}(,\d{3})*$')

commaNRE.search('142')
commaNRE.search('1,234')
commaNRE.search('6,368,745')
commaNRE.search('2,456,368,745')


commaNRE.search('12,68,745')
commaNRE.search('2745')



commaRE = re.compile(r'\d,\d\d\d').search('1,234')




# 21

wataRE = re.compile(r'^[A-Z]\w+ Watanabe$')

wataRE.search('Haruto Watanabe')
wataRE.search('Alice Watanabe')
wataRE.search('RoboCop Watanabe')


wataRE.search('haruto Watanabe')
wataRE.search('Mr. Watanabe')
wataRE.search('Watanabe')
wataRE.search('Haruto watanabe')




# 22

senRE = re.compile(r'''(
    (Alice|Bob|Carol)\s
    (eats|pets|throws)\s
    (apples|cats|baseballs)
    \.
    )''',re.I|re.X)


senRE.search('Alice eats apples.')
senRE.search('Bob pets cats.')
senRE.search('Carol throws baseballs.')
senRE.search('Alice throws apples.')
senRE.search('BOB EATS CATS.')


senRE.search('RoboCop eats apples.')
senRE.search('ALICE THROWS FOOTBALLS.')
senRE.search('Carol eats 7 cats.')







































