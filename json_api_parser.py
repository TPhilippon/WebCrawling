#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 18:24:26 2018

@author: terencephilippon
"""

import bs4
from urllib.request import urlopen as uReq

import json
from pprint import pprint

from urllib.request import Request, urlopen
import numpy as np
import pandas as pd


my_url = 'https://www.fablabs.io/labs'
url_makery = 'http://www.makery.info/api/labs/'
url_fablabs = 'https://api.fablabs.io/v0/labs.json'

makery_file = '/Users/terencephilippon/Desktop/labs.json'
fablabs_file = '/Users/terencephilippon/Desktop/labs.json'

# =============================================================================
# Import and read json page.
# =============================================================================

#Import the whole page.
#req = Request(url_fablabs, headers={'User-Agent': 'Mozilla/5.0'})
#webpage = urlopen(req).read()

#html parsing
data = json.load(open(makery_file))
#Exemple de path pour aller chercher les données.
data["features"][0]["geometry"]
#Numpy array
my_array = np.empty([len(data["features"]),6], dtype=object)

i = 0
for data_part in data["features"]:
    my_array[i,0] = data_part["properties"]["name"]
    my_array[i,1] = data_part["geometry"]["coordinates"][0]
    my_array[i,2] = data_part["geometry"]["coordinates"][1]
    my_array[i,3] = data_part["properties"]["type_lab"]
    my_array[i,4] = data_part["properties"]["adress"]
    my_array[i,5] = data_part["properties"]["country"]
    
    i += 1

df = pd.DataFrame(my_array)
df.to_csv('/Users/terencephilippon/Desktop/makery_data.csv')

# =============================================================================
# ####### Alternate if blocked by server #######
# =============================================================================
req = Request('https://www.fablabs.io/labs', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

page_soup = soup(webpage, "html.parser")

#### testeur
my_url = 'http://www.seloger.com/list.htm?tri=initial&idtypebien=2,1&idtt=2,5&naturebien=1,2,4&ci=60088&LISTING-LISTpg=7'

req = Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

page_soup = soup(webpage, "html.parser")

dd = page_soup.div.a.findAll("c-pa-link link_AB")
#### testeur

decoded_response = page_soup.read().decode("UTF-8")

# =============================================================================
# ####### #######
# =============================================================================




