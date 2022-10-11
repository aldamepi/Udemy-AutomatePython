#! /Users/albertomengual/opt/anaconda3/bin/python
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 18:15:52 2022

@author: albertomengual

Project: Opening All Search Results

Open the first several links in a bunch of new tabs to read later

Type a search term on the command line and have my computer automatically open 
a browser with all the top search results in new tabs.

Let's do this with the search results for Python Package Index at https://pypi.org/

DESCRIPTION
1. Gets search keywords from the command line arguments
2. Retrieves the search results page
3. Opens a browser tab for each result

CODE
1. Read the command line arguments from sys.argv
2. Fetch the search result page with the requests module
3. Find the links to each search result
4. Call the webbrowser.open() function to open the web browser


"""

# import libraries

import sys, os
import requests
import bs4
import webbrowser as wb
import logging


logging.basicConfig(level=logging.DEBUG, 
                    format=' %(asctime)s -  %(levelname)s -  %(message)s')

#logging.disable(logging.CRITICAL)

logging.debug('Start of program')




# Handle the command line arguments

### Running an applescript that requires the search terms and run this py

if len(sys.argv) > 1:
    # Get address from command line
    searchTerms = ' '.join(sys.argv[1:])
    logging.debug('The command line arguments are: %s' %(searchTerms))


else: 
    searchTerms = input('Enter search terms: ')
    # logging.error('No search terms available')
    # raise Exception ('No search terms available')
    # sys.exit()



# Prepare the search terms to the address line    
searchTerms = searchTerms.replace(' ', '+')
logging.debug('The web address\' search terms are: %s' %(searchTerms))



# Open the search in the browser
## Variables
address0 = 'https://pypi.org/search/?q='
searchAddress = address0 + searchTerms

## Code
wb.open(searchAddress)






# Fetch the search result page with the request module

searchRes = requests.get(searchAddress)

searchRes.raise_for_status()




# Parse the search page
    
sSoup = bs4.BeautifulSoup(searchRes.text, 'lxml')


# Find the links

## Number of links

nLinks = 5

##### ¿Que pasaría si la busqueda no tiene resultados?

for i in range(1,nLinks+1):
    linkSet = sSoup.select('.unstyled > li:nth-child(%s) > a:nth-child(1)' %(i))
    
    # len(linkSet)    
    # str(linkSet[0])    
    # linkSet[0].getText()    
    # linkSet[0].attrs
    
    newTabLink = linkSet[0].get('href')
        
    # Open the search in a new tab    
    address1 = 'https://pypi.org'
    newTab = address1 + newTabLink
    logging.debug('The new Tab\'s address is : ' + newTab)
    
    wb.open(newTab)



logging.debug('End of program')



######### Book Answer

# linkSet2 = sSoup.select('.package-snippet')

# len(linkSet2)
# linkSet2[2].attrs

# nOpen = min(5,len(linkSet2))

# for i in range(nOpen):
#     urlToOpen = 'https://pypi.org' + linSet2[i].get('href')
#     print('Opening', urlToOpen)
#     wb.open(urlToOpen)









































