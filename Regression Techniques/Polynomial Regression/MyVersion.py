#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 12:03:03 2019

@author: saeed
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

dataset = pd.read_csv('Position_Salaries.csv')


X = dataset.iloc[:,1:2].values
y = dataset.iloc[:,-1].values


### we don't split the data into train/test because we only have 10 data points
### due to small number of observations, it is recommended to use all the data points
### to train the model to have a more accurate model. 

### feature scaling is not necessary as LinearRegression model in scikit-learn
### takes care of that part for us. 


from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X,y)

y_pred = lin_reg.predict(X)

## Visualization
plt.scatter(X,y, color = 'red')
plt.plot(X,y_pred, color = 'blue')
plt.title('Salary vs. Level')
plt.xlabel('Level')
plt.ylabel('Salary')


### we could have done this step differently by directly adding different degrees
### of independent variables to the dataset. However, in Python, scikit-learn has
### automated this job for us with PolynomialFeatures class. 
from sklearn.preprocessing import PolynomialFeatures
polyfeat = PolynomialFeatures(4)
X_poly = polyfeat.fit_transform(X)

lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly,y)

y_pred2 = lin_reg_2.predict(X_poly)

## Visualization
plt.scatter(X,y, color = 'red')
plt.plot(X,y_pred2, color = 'blue')
plt.title('Salary vs. Level')
plt.xlabel('Level')
plt.ylabel('Salary')

