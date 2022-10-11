#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 23:13:56 2022

@author: albertomengual

Pig Latin is a silly made-up language that alters English words.
If a word begins with a vowel, the word yay is added to the end of it.
If a word begins with a consonant or consonant cluster (like ch), that 
consonant or cluster is moved to the end of the word followed by ay.

Enter the English message to translate into Pig Latin:
My name is AL SWEIGART and I am 4,000 years old.
Ymay amenay isyay ALYAY EIGARTSWAY andyay Iyay amyay 4,000 yearsyay oldyay.

"""


############################## ALGORYTHM

# prompt the message to be translated

# Define the vowels

# Create a list where the translated words will be added: pigLatin

# Begin a loop will go trough every word of the initial message:
    # Separete non-letter prefixes of the word:
        # Create a word without prefix and the prefix
        # There is not such a word but just the non-letter prefix...add it
    
    # Separate non-letter suffixes to the word:
        # Create a word without the suffix and the suffix
    
    # Record if the letter was in uppercase or titlecase.
    
    # Make the word lowercase for translation
    
    # Separate the consonants at the beginning of the word:
        # Create a consonant prefix and a word without consonant.
    
    # Add the pig latin ending:
        # consonant + ay
        # (when vowels) + yay
    
    # Set the word back to uppercase of title cse
    
    # Add the non-letters back to the beginning and end of the word
    
# Join the words in a single string
    
    
    



################################### CODE

message = input('Enter the text to be translated into Pig Latin: \n')

vowels = ('a', 'e', 'i', 'o', 'u', 'y')

# Is there any library to include vowels or other characters to lists????

pL = []


for word in message.strip().split():
    
    # Separate non-letter prefixes
    nonLpre = ''
    # while not word[0].isalpha(): # it is necessary to include first len>0
                                   # otherwise: IndexError 
    #     nonLpre += word[0]
    #     word = word[1:]
    #     if len(word) == 0: # It is necessary to take it out the loop to work
                             # after the condition len>0 in the loop
    #         pL.append(nonLpre)
    #         continue

    while len(word)>0 and not word[0].isalpha():
        nonLpre += word[0]
        word = word[1:]
    if len(word) == 0:
        pL.append(nonLpre)
        continue # it avoids future indexErrors
    
    # Separate non-letter suffixes to the word
    nonLSu =''
    while not word[-1].isalpha():
        nonLSu += word[-1]
        word = word[:-1]
    
    # Record the letter case
    wasUpper = word.isupper()
    wasTitle = word.istitle()
    
    word = word.lower()
    
    # Separate the consonants 
    conPre = ''
    if word[0] not in vowels: # It is possible not to write this if here and
                              # write it later in the ending adding.  
        while word[0] not in vowels:
            conPre += word[0]
            word = word[1:]
        
        # Add the pig latin ending
        word = word + conPre + 'ay'
    
    else:
        word += 'yay'
    
    # Set back the word case
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()
    
    # Restore the non-letters prefixes and suffixes
    word = nonLpre + word + nonLSu
    
    pL.append(word)

# Join words to string
pigMessage = ' '.join(pL)

print(pigMessage)

        
        








































































































