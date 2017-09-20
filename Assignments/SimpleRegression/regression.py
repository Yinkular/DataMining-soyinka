# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 00:01:29 2017

@author: soyinka
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# preprocessing
# import data set
dataset = pd.read_csv('mortgage_rates.csv')

# replace unwanted characters
# make salary an integer value
dataset.iloc[:,2] = dataset.iloc[:,2].str.replace(',','')
dataset.iloc[:,2] = dataset.iloc[:,2] .str.replace('$','')
dataset.iloc[:,2]  = dataset.iloc[:,2] .astype(int)

# get dependent and independent variables
x = dataset.iloc[:,1:2]
y = dataset.iloc[:,2] #vector



#split data
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=1/4, random_state=0)


#operation
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)

#test
y_pred = regressor.predict(x_test)
