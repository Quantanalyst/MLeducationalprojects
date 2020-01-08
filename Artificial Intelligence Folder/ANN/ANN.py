'''

Date: Jan. 01 2020
Author: Saeed Mohajeryami, PhD

'''

import numpy as np
import pandas as pd

dataset = pd.read_csv('Churn_Modelling.csv')

X = dataset.iloc[:,3:13].values
y = dataset.iloc[:,-1].values


### categorical variables
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
encoder_gender = LabelEncoder()
encoder_country = LabelEncoder()
X[:,1] = encoder_country.fit_transform(X[:,1])
X[:,2] = encoder_gender.fit_transform(X[:,2])

onehotencoder = OneHotEncoder(categorical_features = [1])
X = onehotencoder.fit_transform(X).toarray()

X = X[:,1:]

### train/test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

### feature scaling
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


### ANN
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout

classifier = Sequential()

#----------------------------------------------------------------
#  MODEL CREATION
#----------------------------------------------------------------
## adding the input layer and first hidden layer
classifier.add(Dense(6, kernel_initializer='uniform', activation='relu', input_dim = 11))
classifier.add(Dropout(rate = 0.1))
## second hidden layer
classifier.add(Dense(6, kernel_initializer='uniform', activation='relu'))
classifier.add(Dropout(rate = 0.1))
## output layer
classifier.add(Dense(1, kernel_initializer='uniform', activation='sigmoid'))
#----------------------------------------------------------------

#----------------------------------------------------------------
#  MODEL COMPILATION
#----------------------------------------------------------------
## compile the model
classifier.compile(optimizer='adam', loss='binary_crossentropy',metrics=['accuracy'])
#----------------------------------------------------------------

#----------------------------------------------------------------
#  MODEL FIT
#----------------------------------------------------------------
## compile the model
classifier.fit(X_train, y_train, batch_size=10 , epochs=5)
#----------------------------------------------------------------

#----------------------------------------------------------------
#  MODEL PREDICT
#----------------------------------------------------------------
## compile the model
y_pred = classifier.predict(X_test)
y_pred = y_pred > 0.5
#----------------------------------------------------------------

from sklearn.metrics import confusion_matrix, accuracy_score
print(accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))


## check if a customer with a below properties leave the bank?
lst = [600,'France','Male',40,3,60000,2,1,1,50000]
XX = pd.DataFrame([lst])
XX.iloc[:,1] = encoder_country.transform(XX.iloc[:,1])
XX.iloc[:,2] = encoder_gender.transform(XX.iloc[:,2])
XX = onehotencoder.transform(XX).toarray()
XX = XX[:,1:]
XX = scaler.transform(XX)

res = classifier.predict(XX)


#----------------------------------------------------------------
#  K-fold Cross Validation - Evaluation of the model
#----------------------------------------------------------------
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score
from keras.models import Sequential
from keras.layers import Dense
def build_classifier():
    classifier = Sequential()
    classifier.add(Dense(6, kernel_initializer='uniform', activation='relu', input_dim = 11))
    classifier.add(Dropout(rate = 0.1))
    classifier.add(Dense(6, kernel_initializer='uniform', activation='relu'))
    classifier.add(Dropout(rate = 0.1))
    classifier.add(Dense(1, kernel_initializer='uniform', activation='sigmoid'))
    classifier.compile(optimizer='adam', loss='binary_crossentropy',metrics=['accuracy'])
    return classifier
classifier = KerasClassifier(build_fn = build_classifier, batch_size=50 , epochs=2)
accuracies = cross_val_score(classifier, X = X_train, y = y_train, cv = 10, n_jobs=-1)

accuracy_mean = accuracies.mean()
accuracy_variance = accuracies.std()

#----------------------------------------------------------------
#  ANN - Parameter Tuning
#----------------------------------------------------------------
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import GridSearchCV
from keras.models import Sequential
from keras.layers import Dense
def build_classifier(optimizer):
    classifier = Sequential()
    classifier.add(Dense(6, kernel_initializer='uniform', activation='relu', input_dim = 11))
    classifier.add(Dropout(rate = 0.1))
    classifier.add(Dense(6, kernel_initializer='uniform', activation='relu'))
    classifier.add(Dropout(rate = 0.1))
    classifier.add(Dense(1, kernel_initializer='uniform', activation='sigmoid'))
    classifier.compile(optimizer=optimizer, loss='binary_crossentropy',metrics=['accuracy'])
    return classifier
classifier = KerasClassifier(build_fn = build_classifier, batch_size=50 , epochs=2)
parameters = {'batch_size':[20,40,60],
              'epochs':[1,2,3],
              'optimizer':['adam','rmsprop']}
grid_search = GridSearchCV(estimator=classifier,
                           param_grid=parameters,
                           scoring='accuracy',
                           cv = 10,
                           n_jobs=-1)
grid_search = grid_search.fit(X = X_train, y= y_train)
best_parameters = grid_search.best_params_
best_accuracy = grid_search.best_score_
