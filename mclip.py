#! /Users/albertomengual/opt/anaconda3/bin/python
"""
#!/usr/bin/env python3
"""
# -*- coding: utf-8 -*-

"""
#! is called shebang line

Created on Mon Feb 28 18:30:45 2022
@author: albertomengual

Frist Project out of the Automate The Boring Stuff with Python's book.
Originally named mclip.py - A multi-clipboard program.

This program stores multiple phrases that will be sent to the clipboard 
through the command line with a short key phrase.

"""


' MULTI-CLIPBOARD AUTOMATIC MESSAGES '.center(78,'#')
##################### MULTI-CLIPBOARD AUTOMATIC MESSAGES #####################

import sys, pyperclip







# Create a dictionary to stores keyphrases and text

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}




# Handle Command Line Arguments: Display usage message

if len(sys.argv) < 2: # in case any keyphrase specified
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

"""
sys.argv:
La lista de argumentos de la línea de comandos pasados a un script de Python. 
argv[0] es el nombre del script ('mclip.py') (depende del sistema operativo 
si se trata de una ruta completa o no).
"""    
# depending on the keyphrase a message will be copied to the clipboard
keyphrase = sys.argv[1] # first command line argument is the keyphrase
# keyphrase = 'agree'




# Copy the right pharse

# Check if the keyphrase exixts in the dictionary
    # If so, copy the value to pyperclip.copy()


if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for %s copied to clipboard.' % (keyphrase))
    
else:
    print('That keyphrase is not available.')
    

    
































































































