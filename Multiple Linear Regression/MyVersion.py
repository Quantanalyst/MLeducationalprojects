#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 01:36:47 2019

@author: saeed
"""

import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt

dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,4].values


### label enconding and one hot encoding
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

## Label Encoding
labelencoder_X = LabelEncoder()
X[:,3] = labelencoder_X.fit_transform(X[:,3])

## One Hot Encoding
onehotencoder_X = OneHotEncoder(categorical_features=[3])
X = onehotencoder_X.fit_transform(X).toarray()

### Avoiding Dummy Variable Trap
X = X[:,1:]


## splitting the dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)



## Feature Scaling
"""from sklearn.preprocessing import StandardScaler
standardscaler = StandardScaler()
X_train = standardscaler.fit_transform(X_train)
X_test = standardscaler.fit_transform(X_test)"""


### Linear Regression
from sklearn.linear_model import LinearRegression
regressor = LinearRegression(normalize=True)
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)



### preparing the model by Backward Elimination 
### For this purpose, we use statsmodels library, which is different
### from sklearn regression model. This library doesn't understand the 
### intercept and we should create an artificial intercept by creating
### a column of ones. The coefficient of this new column will act similar
### to intercept from sklearn library
import statsmodels.regression.linear_model as sm
X = np.append(arr=np.ones((50,1)),values=X, axis=1)

### step 1
X_opt = X[:,[0, 1, 2, 3, 4, 5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
print(regressor_OLS.summary())

### step 2 - we found out that index 1 has the highest P-value and must be dropped
X_opt = X[:,[0, 2, 3, 4, 5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
print(regressor_OLS.summary())

### step 3 - This time index 2 has the highest P-value and must be dropped
X_opt = X[:,[0, 3, 4, 5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
print(regressor_OLS.summary())

### step 3 - This time index 4 has the highest P-value and must be dropped
X_opt = X[:,[0, 3, 5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
print(regressor_OLS.summary())


### step 4 - This time index 5 has the highest P-value and must be dropped
X_opt = X[:,[0, 3]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
print(regressor_OLS.summary())




##### Automatic Backward Elimination
import statsmodels.regression.linear_model as sm
def backwardElimination(x, SL):
    numVars = len(x[0])
    temp = np.zeros((50,6)).astype(int)
    for i in range(0, numVars):
        regressor_OLS = sm.OLS(y, x).fit()
        maxVar = max(regressor_OLS.pvalues).astype(float)
        adjR_before = regressor_OLS.rsquared_adj.astype(float)
        if maxVar > SL:
            for j in range(0, numVars - i):
                if (regressor_OLS.pvalues[j].astype(float) == maxVar):
                    temp[:,j] = x[:, j]
                    x = np.delete(x, j, 1)
                    tmp_regressor = sm.OLS(y, x).fit()
                    adjR_after = tmp_regressor.rsquared_adj.astype(float)
                    if (adjR_before >= adjR_after):
                        x_rollback = np.hstack((x, temp[:,[0,j]]))
                        x_rollback = np.delete(x_rollback, j, 1)
                        print (regressor_OLS.summary())
                        return x_rollback
                    else:
                        continue
    regressor_OLS.summary()
    return x
 
SL = 0.05
X_opt = X[:, [0, 1, 2, 3, 4, 5]]
X_Modeled = backwardElimination(X_opt, SL)