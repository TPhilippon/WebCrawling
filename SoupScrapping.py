#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 22:45:41 2018

Scraping with beautifullsoup.

@author: terencephilippon
"""

import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import numpy as np
import pandas as pd

my_url = 'https://www.fablabs.io/labs'
my_url2 = 'https://placestowork.net/amsterdam'

# =============================================================================
# Import and scrap web page.
# =============================================================================

#Import the whole page.
uClient = uReq(my_url2)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")

#Import all similar data
containers = page_soup.findAll("div",{"class":"item"})

#Import parts of the full data previously imported.
container = containers[0]

#Numpy array
my_array = np.empty([124,4], dtype=object)

j = 0

while j <= 3:
    
    i = 0
    print("j = ", j)
    
    while i <= (len(containers) - 1):
        
        container = containers[i]
        if j == 0:
            my_array[i,j] = container.a.span["data-name"]
        if j == 1:
            my_array[i,j] = container.a.span["data-lat"]
        if j == 2:
            my_array[i,j] = container.a.span["data-lng"]
        if j == 3:
            my_array[i,j] = container.a.span["data-street"]
        
        print("i = ", i)
        i += 1
        
    j += 1        
    
df = pd.DataFrame(my_array)
df.to_csv('/Users/terencephilippon/Desktop/Amsterdam_scrap.csv')

# =============================================================================
# ####### Alternate if blocked by server #######
# =============================================================================
req = Request('https://www.fablabs.io/labs', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

page_soup2 = soup(webpage, "html.parser")
