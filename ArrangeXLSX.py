#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 20:19:45 2018

Arrange XLSX

@author: terencephilippon
"""

import pandas
import os
import numpy as np
from numpy import genfromtxt
import re


path = "/Users/terencephilippon/Desktop/ScrapAmsterdam1_rw2.xlsx"

fillvalue = -99999

myfile = pandas.read_excel(path)
#myfile = genfromtxt(path, delimiter=',')
#myfile=pandas.read_csv(path,sep=',')

#sample = ['?q=@']

# Eliminer premier bloc de chaque colonne.
# 1. Process colonne URL pour récupérer ?q=@ lon lat.
# 2. Process colonne 2 pour récupérer case avec chiffre 1. + case suivante.
# (En compilant tout ça dans 4 colonnes (lon;lat;nom,adresse))

# remove NaN
myfile = myfile.fillna(value=fillvalue)

#myfile[[0,0]][1:20][:]

# Pour colonne 0
A=myfile[[0,]][:]
# Pour colonne 1
B=myfile[[1,]][:]
counter = 0

#==============================================================================
# # Return all cells with google maps GPS data - OK
#==============================================================================
aa = A[A['URL'].str.contains("maps.google")]
# Fill a numpy array with lon lat
arr = np.empty([125,2])

i = 1
while i <= 124 :
    x = str(aa.iloc[i])
  
    arr[i,0] = re.findall("\d+\.\d+",str(aa.iloc[i]))[0]
    print arr[i,0]
    print re.findall("\d+\.\d+",str(aa.iloc[i]))[0]
    arr[i,1] = re.findall("\d+\.\d+",str(aa.iloc[i]))[1]
    print re.findall("\d+\.\d+",str(aa.iloc[i]))[1]
#    arr[i,1] = float(x[])
#    arr[i,0] = float(str(aa.iloc[i])[35:45])

    i += 1

result = arr[:][1:,:]
np.savetxt("/Users/terencephilippon/Desktop/ScrapAmsterdam1_lonlat_OUT.csv",
           result,
           fmt='%f',
           delimiter=',')
#==============================================================================
# # Return all cells with name and adress data
#==============================================================================
B[B['Link'].str.contains("maps.google")]

if re.search(r'\d'+'.', B['Link']):
    print 'yes'


for i in (A['URL'][:]) :
    print i
    print counter
    if any("?q=@" in str(i)):
        print i
        
    counter += 1

### Archive scrip pour hadrien

myfile = myfile.fillna(value=fillvalue)
sample = myfile[[3]]


# Sampling
sample['other_tags,C,254'].str.extract('(\d+)')       # rabot : .astype(int)
sample = sample.fillna(value=fillvalue)

# Sauvegarde du fichier (si ne fonctionne pas, copier coller directement depuis
# l'explorateur de variables vers une feuille de calcul)
pandas.sample.to_scv("/Users/terencephilippon/Desktop/Mreza_da_tri.csv")

#=================================
# Pour enlever davantage de valeurs si nécessaire (importation en numpy)
#my_data = genfromtxt('/Users/terencephilippon/Desktop/Mreza_da_int.csv', delimiter=';')


### Dictionnaire ###

A['URL'][2]
str(A['URL'][2])

test = 'abc1.de'
if any(i.isdigit() for i in test) :
    print 'yes'
    
#1
aa.loc[:].values
#2
str(aa.iloc[120])
    
    
    
