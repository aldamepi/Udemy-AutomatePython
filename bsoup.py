#! /Users/albertomengual/opt/anaconda3/bin/python
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 13:35:41 2022

@author: albertomengual


"""

import requests, bs4



# res = requests.get('https://nostarch.com/automatestuff2/')

# res.raise_for_status()

# theSoup = bs4.BeautifulSoup(res.text, 'lxml')

# type(theSoup)




# resA = requests.get('https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994')

resA = requests.get('https://nostarch.com/automatestuff2/')

resA.raise_for_status()

aSoup = bs4.BeautifulSoup(resA.text, 'lxml')

aPrice = aSoup.select('div.form-type-radio:nth-child(1) > label:nth-child(1)')
elemTest = aSoup.select('#author')



len(aPrice)
len(elemTest)


type(aPrice)
type(aPrice[0])


str(aPrice[0])


aPrice[0].getText()


aPrice[0].attrs

aPrice[0].get('class')
aPrice[0].get('for')
aPrice[0].get('input checked') == None



















































































