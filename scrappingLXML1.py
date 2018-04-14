#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 16:17:55 2018

Scrapping web data via XPATH
Objectif : récupérer des annuaires / listes de Tiers Lieux (ou autre objet)
sur différents sites web.

RMQ : Ne fonctionne pas si google API utilisée / lien fantome ?

@author: terencephilippon
"""

#==============================================================================
# imports & définitions
#==============================================================================

import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from lxml import html
import requests



#==============================================================================
# Core
#==============================================================================

page = requests.get('https://www.fablabs.io/labs')
tree = html.fromstring(page.content)


### Stock Xpaths
xpath1 = "/html/body/article"
all_xpaths = "/html/body/article/div[2]"
all_xpaths2 = "/html/body/article/div[125]"

#Create list 1
list1 = tree.xpath('//article[class="list"]/text()')

list2 = tree.xpath('//div[title="item"]/text()')

list2 = tree.xpath('//body//article[div="2"]/text()')

print list2



