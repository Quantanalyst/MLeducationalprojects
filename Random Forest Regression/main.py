#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 19:52:48 2019

@author: saeed
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators= 1000)

regressor.fit(X,y)

y_pred = regressor.predict([[6.5]])

### visualization
x_grid = np.arange(0,10,0.01)
plt.scatter(X,y, color = 'red')
plt.plot(x_grid, regressor.predict(x_grid.reshape(-1,1)), color='blue')
plt.title('Salary vs. Level')
plt.xlabel('Level')
plt.ylabel('Salary')
plt.show()