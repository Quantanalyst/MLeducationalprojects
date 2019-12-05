#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 11:46:33 2019

@author: saeed
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 


dataset = pd.read_csv('Position_Salaries.csv')

X = dataset.iloc[:,1:2].values
y = dataset.iloc[:,-1].values

from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(3)
X_poly = poly.fit_transform(X)

from sklearn.linear_model import Ridge
ridge_regressor = Ridge(alpha=30)
ridge_regressor.fit(X_poly,y)

from sklearn.linear_model import LinearRegression
linear_regressor = LinearRegression()
linear_regressor.fit(X_poly,y)


### visualization
plt.scatter(X,y, color = 'red')
plt.plot(X,linear_regressor.predict(X_poly), color = 'blue')
plt.plot(X,ridge_regressor.predict(X_poly), color = 'black')