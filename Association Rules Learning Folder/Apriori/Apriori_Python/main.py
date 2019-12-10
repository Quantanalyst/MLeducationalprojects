#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 22:20:49 2019

@author: saeed
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)

# creating a list of lists for dataset
transactions = []
for i in range(0,len(dataset)):
    transactions.append([str(dataset.values[i,j]) for j in range(0,20)])
    
    
## fit apriori algorithm to the dataset
from apyori import apriori
rules = apriori(transactions, min_support = 0.003 , min_confidence = 0.2, min_lift = 3 , min_length = 2)

# visualization
results = list(rules)
