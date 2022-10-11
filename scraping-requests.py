#! /Users/albertomengual/opt/anaconda3/bin/python
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 20:45:38 2022

@author: albertomengual
"""



import requests


# response object
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

# res = requests.get('https://automatetheboringstuff.com/page_not_exists')


# methods
res.status_code # Integer Code of responded HTTP Status
res.status_code == requests.codes.ok # The status code for ok in the HTTP 
                                     # protocol is 200.

# Checking for errors
res.raise_for_status()


# variables
len(res.text)
res.text # Content of the response, in unicode...
print(res.text[:250])


res.url

res.cookies # A cookieJar of cookies the server sent back


# Saving Files to Hard Drive

with open('romeoNJuliet.txt', 'wb') as f:
    for chunk in res.iter_content(100000):
        f.write(chunk)
    f.close()































































































