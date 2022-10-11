#! /Users/albertomengual/opt/anaconda3/bin/python
"""
#!/usr/bin/env python3
"""
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 20:55:43 2022

@author: albertomengual
"""
"""
#! /Users/albertomengual/opt/anaconda3/bin/python
"""


import os, sys


TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}



 # Just write the received parameter into a text file on the Desktop to show how it works
file = os.path.expanduser("~/Desktop/result.txt")
with open(file, 'w') as f:
   f.write(TEXT[sys.argv[1]])










































