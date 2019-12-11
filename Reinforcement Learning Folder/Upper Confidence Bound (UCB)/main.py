#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 15:13:07 2019

@author: saeed
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

    
## visualization of different ads distribution
reward = []
for i in range(0,10):
    reward.append(sum(dataset.iloc[:,i]))
plt.bar(range(1,11),reward)


### Benchmark: Random Selection
import random
N = 10000
d = 10
ads_selected = []
total_reward = 0
for n in range(0, N):
    ad = random.randrange(d)
    ads_selected.append(ad)
    reward = dataset.values[n, ad]
    total_reward = total_reward + reward

# Visualising the results
plt.hist(ads_selected)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()


## UCB algorithm
## step 1
d = 10
number_of_selctions = [0]*d
sum_of_rewards = [0]*d

## step 2
N = 10000
ads_selected = []
total_reward = 0
for n in range(0,N):
    ad = 0
    max_uppoer_bound = 0
    for i in range(0,d):
        if (number_of_selctions[i] > 0):
            ## computing average reward for each arm (ad)
            average_reward = sum_of_rewards[i] / number_of_selctions[i]
            ## computing upper confidence interval for each arm (ad)
            delta_i = math.sqrt (3/2 * math.log(n+1) / number_of_selctions[i])
            upper_bound = average_reward + delta_i
        else:
            upper_bound = 1e400
        if upper_bound > max_uppoer_bound:
            max_uppoer_bound = upper_bound
            ad = i
    ads_selected.append(ad)
    number_of_selctions[ad] = number_of_selctions[ad] + 1
    reward = dataset.values[n,ad]
    sum_of_rewards[ad] = sum_of_rewards[ad] + reward
    total_reward = total_reward + reward


# Visualising the results
plt.hist(ads_selected)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()