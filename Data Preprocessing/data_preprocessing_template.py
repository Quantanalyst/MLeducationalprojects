# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values


### handling missing values 
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values= 'NaN', strategy= 'mean', axis = 0)
X[:,1:3] = imputer.fit_transform(X[:,1:3])

### hot enconding 
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# The first part transforms string categorical values into numerical 
# categorical values. However, these numerical values have order, while
# our string categorical values don't have an order. So, we need to take
# another step called one hot encoding
labelencoder_X = LabelEncoder()
X[:,0] = labelencoder_X.fit_transform(X[:,0])

# one hot encoding creates a column for each categorical value. This way,
# our models can treat the features in a correct way without reading too 
# much into the feature formats
onehotencoder = OneHotEncoder(categorical_features=[0])
X = onehotencoder.fit_transform(X).toarray()

# for labeling dependent variable, we don't need one hot encoding, only
# label encoding is need
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)



# Splitting the dataset into the Training set and Test set
# again, we use scikit learn library and we use train_test_split class
# from model_selection library of sklearn 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y, 
                                                    test_size = 0.2,
                                                    random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train.reshape(-1,1))

