#! /Users/albertomengual/opt/anaconda3/bin/python
# -*- coding: utf-8 -*-
"""

Created on Mon Mar 14 21:49:04 2022


@author: albertomengual

Project: Downloading all xkcd comics

Write a program that copies all the webcomics in https://xkcd.com/ by navigating
through the previous button.

BASIC ALGORITHM
1. Loads the XKCD home page
2. Saves the comic image on that page
3. Follows the previous comic link
4. Repeats until it reaches the first comic


CODE
1. Download pages with the requests module
2. Find the URL of the comic image for a page using bs4
3. Download and save the comic image to the hard drive with iter_content()
4. Find the URL of the Previous Comic link and repeat

"""



# IMPORT LIBRARIES

import sys, os
import webbrowser as wb
import requests
import bs4
import logging

logging.basicConfig(level=logging.DEBUG, 
                    format=' %(asctime)s -  %(levelname)s -  %(message)s')


logging.disable(logging.CRITICAL)


logging.debug('Start of program')




count = 0
pLink = ''
prevLink = 'https://xkcd.com/'

#### Choose a loop: while or for?

while pLink != '#' and count < 15:
# while not prevLink.endswith('#'):     # Book Answer
    logging.debug('Begin loop %s' %(count))
    # Load the home page
    #link0 = 'https://xkcd.com/'
    if pLink == '':
        wb.open('https://xkcd.com/')
    
    
    # Download and parse the page
    print('Downloading page: %s...' %(prevLink))  # Book tip
    res = requests.get(prevLink)
    res.raise_for_status()
    logging.debug('Web site downloaded')
    
    soup = bs4.BeautifulSoup(res.text,'lxml')
    logging.debug('Web site parsed')

    
    # Find the URL of the comic image
    iElem = soup.select('#comic img:nth-child(1)') # It'd download image-links too
    # iElem = soup.select('#comic img')           # Book Answer
    # iElem = soup.select('#comic > img:nth-child(1)')
   
    logging.debug('Image set of length: %s' %(len(iElem)))
    
    if iElem == []:                      # Book Answer
        print('Could not find comic image %s.' % (fn))
    
    # len(iElem)
    # iElem[0].attrs
    # iElem[0].get('src')
    
    comicURL = 'https:' + iElem[0].get('src')
    # except IndexError:
    #     print('Image %s is probably an Ad with a link.' %(fn))
    #     count += 1
    #     continue
    
    # Download and save the image to a file
    print('Downloading image %s...' %(os.path.basename(comicURL)))    # Book Answer (with file extension)
    imgRes = requests.get(comicURL)
    imgRes.raise_for_status()
    logging.debug('Comic Image site downloaded')
    
    ## Give a name to the file:
    if pLink == '':
        fName1 = soup.select('#middleContainer > a:nth-child(6)')           
        # len(fName1)
        # fName1[0].attrs
        fn = fName1[0].getText()       
        fn = fn.rsplit('/',2)[1]
        
    #imageFile = open(os.path.join('comics', os.path.basename(comicUrl)),'wb')
    # fn = os.path.basename(comicUrl)         # Book answers
    
    with open(os.path.join('comics', '%s.png' %(fn)), 'wb') as f:   # paths with os.path.join
        for chunk in imgRes.iter_content(100000):
            f.write(chunk)
        f.close()
    logging.debug('Saved comic %s into file %s' %(os.path.basename(comicURL),fn))
    
    
    
    # Find the link to the previous
    
    prevElem = soup.select('ul.comicNav:nth-child(4) > li:nth-child(2) > a:nth-child(1)')
    # prevElem = soup.select('a[rel="prev"]')[0]     # Book Answer 
    # len(prevElem)
    # prevElem[0].attrs
    
    pLink = prevElem[0].get('href')
    
    ## Name the file in previous
    fn = pLink.strip('/')
    
    prevLink = 'https://xkcd.com' + pLink
    
    logging.debug('End loop %s' %(count))
    count +=1
    
print('Done.')
logging.debug('End of program')




###### Test Code






























































































