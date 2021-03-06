# -*- coding: utf-8 -*-
"""extratree_models_score.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jdTy2_pGgqV_nhQUXF7ZAsFWqF7ObjlY

## 1. Loading Data and Packages
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import warnings
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.metrics import accuracy_score,mean_squared_error,r2_score,mean_absolute_error
from math import sqrt
warnings.filterwarnings('ignore')

from google import colab
colab.drive.mount('/content/gdrive')

# Load train and Test set
import os 
path = '/content/gdrive/My Drive/colab/credit_score_zalda'

data = pd.read_csv(path+'/loan_data.csv')

r = 0.13
interestRate=r/data['Number_of_installments(months)']
data['loan_limit']            = abs(np.pv(interestRate/data['Number_of_installments(months)'],

                                data['Number_of_installments(months)']*1,

                                data['monthly_installments'],

                                when='end').round(0)
)

data.head()

objList=data.select_dtypes(include='object')

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

for feat in objList:
    data[feat] = le.fit_transform(data[feat].astype(str))

print (data.info())

X=data.drop(['Score','loan_limit'],1)
Y=data[['Score','loan_limit']]

X.shape, Y.shape

"""## 6. Modeling and Predictions"""

# !pip install catboost

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state=300)

etree=ExtraTreesRegressor(random_state=2)
etree.fit(x_train,y_train)
y_pred=etree.predict(x_test)

MAE=mean_absolute_error(y_test,y_pred),
RMSE=np.sqrt(mean_squared_error(y_test,y_pred)),
R2_SCORE=r2_score(y_test, y_pred)
print(MAE,RMSE,R2_SCORE)

pred=np.int_(etree.predict(data.drop(['Score','loan_limit'],axis=1)))

pred=pd.DataFrame(pred, columns=['Score_pred','loan_limit_pred'])
pred['Score']=data['Score']
pred['loan_limit']=data['loan_limit']
pred.head(20)

pred.shape

# Import pickle Package

import pickle

# Save the Modle to file in the current working directory
Pkl_Filename = "Pickle_RL_Model.pkl"  

with open(Pkl_Filename, 'wb') as file:  
    pickle.dump(etree, file)

# Load the Model back from file
with open(Pkl_Filename, 'rb') as file:  
    Pickled_ET_Model = pickle.load(file)

Pickled_ET_Model

x_train.info()