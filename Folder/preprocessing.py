# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('TempDataset.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 13].values

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

print(dataset.iloc[:, 8].values)
print(X[:,8])

#debug
for column in dataset.columns:
    if dataset[column].dtype == type(object):
        #le = LabelEncoder()

        #dataset[column] = le.fit_transform(dataset[column])
        
        
# Encoding categorical data
# Encoding the Independent Variable
column = 8
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

labelencoder_X = LabelEncoder()
if X[:, column].dtype == type(object):
    X[:, column] = labelencoder_X.fit_transform(X[:, column])

try:
    
    if X[:, column].dtype == type(object):
        onehotencoder = OneHotEncoder(categorical_features = [column])
        X = onehotencoder.fit_transform(X).toarray()
except ValueError:
    pass        

# Encoding the Dependent Variable
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)