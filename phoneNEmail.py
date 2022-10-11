#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 19:19:13 2022

@author: albertomengual

Phone and email adress extractor

## Need to do:
Get the text of the clipboard
Find all phone numbers and email addresses in the text:
    American phone number: +1 415.863.9900
    email: someemail@server.com
Paste them onto the clipboard


## Algorythm in Code:
Use the pyperclip module to copy and paste strings.
Create two regexes, one for matching phone numbers and the other for matching email addresses.
Find all matches, not just the first match, of both regexes.
Neatly format the matched strings into a single string to paste.
Display some kind of message if no matches were found in the text.

"""


# Import the libraries
import pyperclip as ppc
import re



# Paste the copied text
ts = str(ppc.paste())




# Create the regular expression for the phone numbers

phoneRE = re.compile(r'''(
    (\+\d+)?              # International code
    [ -/.]                # separator
    (\d{3})               # are code
    [ -/.]                # separator
    (\d{3})               # first 3 digits
    [ -/.]                # separator
    (\d{4})               # last 4 digits
    )''', re.X)


# Create regular expression for the emails


# emailRE = re.compile(r'''(
#     [\w\-+.%]+     # username
#     @              # @
#     [-\w+.]+       # domain
#     \.com          # emails.com
#     )''',re.X)

emailRE = re.compile(r'''(
    [\w\-+.%]+             # username
    @                      # @
    [-\w+.]+               # domain
    \.[a-zA-Z]{2,4}        # dot-something
    )''',re.X)



# Find the matches

phones = phoneRE.findall(ts)

emails = emailRE.findall(ts)



# Clean and format the matches

#phonesNeat = []
for i,t in enumerate(phones):
    phones[i] = '-'.join(t[2:])

phonesS = '\n'.join(phones)

emailsS = '\n'.join(emails)

finalString = phonesS + '\n' + emailsS
# finalString = '\n'.join([phonesS] + [emailsS])


# Final message and Copy to the clipboard

if len(phones)!=0 or len(emails)!=0:
    ppc.copy(finalString)
    print('Copied to clipboard:')
    print(finalString)
else:
    print('No phone numbers or email addresses found.')




# Test code


# print(phones)
# print(emails)





































































































