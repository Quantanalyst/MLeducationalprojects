#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 14:32:40 2019

@author: saeed
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset = pd.read_csv('Churn_Modelling.csv')

X = dataset.iloc[:,3:13].values
y = dataset.iloc[:,13].values

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
## label encoding geography and gender
labelencoder_geography = LabelEncoder()
X[:,1] = labelencoder_geography.fit_transform(X[:,1])
labelencoder_gender = LabelEncoder()
X[:,2] = labelencoder_gender.fit_transform(X[:,2])
## one hot encoding the labels of geography
## since gender has only two category, it doesn't need one hot encoding
## so, the good thing is we have one less categorical feature for handling
## the categorical feature trap
onehotencoder = OneHotEncoder(categorical_features=[1])
X = onehotencoder.fit_transform(X).toarray()

## removing one feature to avoid dummy variable trap
X = X[:,1:]

### train/test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

### scaling the data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


### import keras
import keras
from keras.models import Sequential
from keras.layers import Dense

### initializing the ANN
classifier = Sequential()

### Adding the input layer and first hidden layer
classifier.add(Dense(output_dim = 6, init = 'uniform', activation = 'relu', input_dim = 11))

### Adding the second hidden layer
classifier.add(Dense(output_dim = 6, init = 'uniform', activation = 'relu'))

### Adding the output layer
classifier.add(Dense(output_dim = 1, init = 'uniform', activation = 'sigmoid'))
                     
### compiling the ANN
classifier.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

### Fitting the ANN to the training data
classifier.fit(X_train, y_train, batch_size=10, nb_epoch=100)   

### prediction
y_pred = classifier.predict(X_test)

y_pred = (y_pred > 0.5)

from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
print(confusion_matrix(y_test, y_pred))
print(accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
                
                     
                     