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
2. Open yandex login site (gmail e icloud no me dejan)
3. Fill username
4. Fill password
4.2 Fill phone code
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



# DEV INPUT
emailTo = st.emailGestion
bodyText = 'Esto es un mensaje de prueba'





# OPEN BROWSER TO YANDEX LOGIN SITE
browser = webdriver.Firefox()
browser.get('https://passport.yandex.com/auth')

# FILL USERNAME
userForm = browser.find_element_by_css_selector('#passp-field-login')
# DeprecationWarning: find_element_by_css_selector is deprecated. 
# Please use find_element(by=By.CSS_SELECTOR, value=css_selector)
# userForm = browser.find_element(by='css selector', value='#account_name_text_field')
# userForm = browser.find_element_by_css_selector('#identifierId')
userForm.send_keys(st.emailYandex)
userForm.submit()

# siguiente = browser.find_element_by_css_selector('button')
# siguiente.click()


# FILL PASSWORD
passForm = browser.find_element_by_id('passp-field-passwd')
passForm.send_keys(st.yandexPassword)
passForm.submit()

# CONFIRM PHONE CODE SENDING
Confirm = browser.find_element_by_class_name('Button2')
#Confirm = browser.find_element_by_css_selector('.Button2')
Confirm.click()

# FILL PHONE CODE
################ Is it possible to control sms with python??
phoneCode = browser.find_element_by_id('passp-field-phoneCode')
phoneCode.send_keys('834-588')
phoneCode.submit()


# GO TO COMPOSE EMAIL SITE (https://mail.yandex.com/compose)
account = browser.find_element_by_class_name('user-account_has-ticker_yes')
account.click()

compose = browser.find_element('class name', 'legouser__menu-item_action_mail-compose')
# compose = browser.find_element('link text', 'Compose message') # also valid
compose.click()

# browser.get('https://mail.yandex.com/compose') # also valid


# COMPOSE AND SEND EMAIL
## ADD THE ADDRESSE'S EMAIL ADDRESS

# toForm = browser.find_element('xpath', 
#                               '/html/body/div[2]/div[2]/div[10]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[1]/div[1]/div[1]/div/div/div/div/div')
toForm = browser.find_element('css selector', '.ComposeRecipients-ToField > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)')
toForm.send_keys(emailTo)

## ADD THE BODY TEXT
bodyForm = browser.find_element('class name', 'cke_wysiwyg_div')
bodyForm.click()
bodyForm.send_keys(bodyText)

## ADD THE SUBJECT
subjectForm = browser.find_element('css selector', '.composeTextField')
subjectForm.send_keys('asunto de prueba')

## SEND IT
sendButton = browser.find_element('class name', 'Button2_view_default')
sendButton.click()


## ANTI SPAM FILTER
antiSpam = browser.find_element('class name', 'ComposeReactCaptcha-Input')
antiSpam.send_keys('ourselvesgreen')

send2 = browser.find_element('class name', 'button2_size_m')
send2.click()

##### CTRL + ENTER to send messages


# CLOSE SESSION
account = browser.find_element_by_class_name('user-account_has-ticker_yes')
account.click()

lOut = browser.find_element('css selector', '.legouser__menu-item_action_exit > span:nth-child(1)')
lOut.click()


# subjectForm.clear()
# browser.back()


# CLOSE BROWSER
browser.quit()



logging.debug('End of program.')





























































