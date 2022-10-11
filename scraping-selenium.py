#! /Users/albertomengual/opt/anaconda3/bin/python
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 18:58:24 2022

@author: albertomengual
"""

import os

from selenium import webdriver

browser = webdriver.Firefox(executable_path='/Users/albertomengual/opt/anaconda3/bin/geckodriver')

browser = webdriver.Firefox()

browser.get('https://inventwithpython.com')
browser.get('https://automatetheboringstuff.com')
#browser.get('https://www.facebook.com/')

type(browser)


elem = browser.find_element_by_link_text('Introduction')

elem.tag_name
elem.get_attribute('href')
elem.text

elem.clear() # for text filed or text area elemnts

elem.is_displayed()
elem.is_enabled() # For input elements

elem.is_selected() # For checkbox or radio button elements

elem.location



elem.click()
























































































