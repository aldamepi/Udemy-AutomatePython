#! /Users/albertomengual/opt/anaconda3/bin/python
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 19:28:16 2022

@author: albertomengual

COMMAND LINE EMAILER

Takes an email and string of text on the command line and then, using selenium,
logs in and send an email of the string.

notes: would be a nice way to add a notification feature to the programs
more practice: could also write similar program from Facebook or Twitter

BASIC ALGORITHMN
0. Handle Arguments from command line
1. Open a browser (firefox)
2. Open gmail login site
3. Fill username
4. Fill password
5. Open a new email
6. Add the To email and the body
7. Send it
8. Close session and browser
9. Create apple script to prompt the arguments


"""

##### gmail no me deja iniciar sesión con selenium


import setting as st
import sys
# import os
# import webbrowser as wb
# import requests
# import bs4
from selenium import webdriver
import logging





logging.basicConfig(level=logging.DEBUG, 
                    format=' %(asctime)s -  %(levelname)s -  %(message)s')


# logging.disable(logging.CRITICAL)


logging.debug('Start of program.')



# INPUT VALIDATION
# if len(sys.argv) == 3:
#     emailTo = sys.argv[1]
#     bodyText = sys.argv[2] #How to pass arguments with spaces??? with ""?
#     logging.debug('The addressee\'s email is: %s' %(emailTo))
#     logging.debug('The body of the email is: \n%s' %(bodyText))
# else:
#     raise Exception('The number of arguments is incorrect.')

###### I could also validate the format of the To email with regex





# OPEN BROWSER TO GMAIL LOGIN SITE
browser = webdriver.Firefox()
browser.get('https://accounts.google.com/signin/v2/identifier?')

# FILL USERNAME
userForm = browser.find_element_by_id('identifierId')
# userForm = browser.find_element_by_css_selector('#identifierId')
userForm.send_keys('almepi80')
userForm.submit()

siguiente = browser.find_element_by_css_selector('button')
siguiente.click()



head = browser.find_element_by_css_selector('#headingSubtext span')
recuMens = 'Introduce tu número de teléfono o tu dirección de correo electrónico \
de recuperación'

if head.text == recuMens:
    recuForm = browser.find_element_by_id('recoveryIdentifierId')
    recuForm.send_keys(st.recoveryPhone)
    siguiente = browser.find_element_by_css_selector('button')
    siguiente.click()



head2 = browser.find_element_by_css_selector('#headingText span')
headMens = '¿Cómo te llamas?'

if head2.text == headMens:
    nameForm = browser.find_element_by_id('firstName')
    nameForm.send_keys(st.firstName)
    surnForm = browser.find_element_by_id('lastName')
    surnForm.send_keys(st.lastName)
    siguiente = browser.find_element_by_css_selector('button')
    siguiente.click()



head3 = browser.find_element_by_css_selector('#headingText span')
head3Mens = 'Obtener un código de verificación'

if head3.text == head3Mens:
    siguiente = browser.find_element_by_css_selector('button')
    siguiente.click()


head4 = browser.find_element_by_css_selector('#headingText span')
head4Mens = 'Escribe el código'

if head4.text == head4Mens:
    nameForm = browser.find_element_by_id('idvPin')
    nameForm.send_keys('408803')
    siguiente = browser.find_element_by_css_selector('button')
    siguiente.click()
    

account = browser.find_element_by_css_selector('div[data-email="almepi80@gmail.com"]')
account.click()


##### gmail no me deja iniciar sesión con selenium


browser.quit()



logging.debug('End of program.')





























































