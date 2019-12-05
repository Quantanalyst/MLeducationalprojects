#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 14:13:55 2019

@author: saeed
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('Position_Salaries.csv')

X = dataset.iloc[:,1:2].values
y = dataset.iloc[:,-1].values

## no need for train/test split as the data is super small

## we need feature scaling as SVR doesn't have internal feature scaling
from sklearn.preprocessing import StandardScaler
scaler_X = StandardScaler()
scaler_y = StandardScaler()
X = scaler_X.fit_transform(X)
y = scaler_y.fit_transform(y.reshape(-1,1))


### SVR
from sklearn.svm import SVR
svregressor = SVR(kernel='rbf')
svregressor.fit(X,y)

### An employee from a different company with level 6 and 2 years of experience
### claims that he/she has earned 160k and wants the same level of compensation
### in the new company. Check whether an employee has bluffed or not?
X_target = scaler_X.transform(np.array([[6.5]]))
y_pred = scaler_y.inverse_transform(svregressor.predict(X_target))

# the SVR prediction says 170k

### visualization
plt.scatter(X,y, color = 'red')
plt.plot(X, svregressor.predict(X), color = 'blue')
plt.title('Salary vs. Level')
plt.xlabel('Level')
plt.ylabel('Salary')
plt.show()