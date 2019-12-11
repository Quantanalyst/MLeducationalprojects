
"""
Author : Saeed Mohajeryami, PhD

"""
## Thompson sampling Example

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
import math

# Importing the dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

    
## visualization of different ads distribution
reward = []
for i in range(0,10):
    reward.append(sum(dataset.iloc[:,i]))
plt.bar(range(1,11),reward)


### Benchmark: Random Selection
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


## Thompson Sampling algorithm
d = 10
N = 10000
number_of_reward_1 = [0]*d
number_of_reward_0 = [0]*d

ads_selected = []
total_reward = 0
for n in range(0,N):
    ad = 0
    max_random = 0
    for i in range(0,d):
        random_beta = random.betavariate(number_of_reward_1[i]+1,number_of_reward_0[i]+1)
        if random_beta > max_random:
            max_random = random_beta
            ad = i
    ads_selected.append(ad)
    reward = dataset.values[n,ad]
    if reward == 1: 
        number_of_reward_1[ad] +=1
    else:
        number_of_reward_0[ad] +=1
    total_reward = total_reward + reward


# Visualising the results
plt.hist(ads_selected)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()