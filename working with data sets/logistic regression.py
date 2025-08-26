# Logistic Regression is used for binary classification (output is 0 or 1, like "spam" or "not spam"). It predicts the probability that a data point belongs to a particular class.
# Instead of using a straight line like linear regression, logistic regression uses the sigmoid function to map predictions between 0 and 1:

# importing te libararies 

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt # matplotlib.pyplot This is a module inside matplotlib specifically designed to mimic MATLAB-style plotting. It provides a simple interface to create common charts like line plots, bar plots, scatter plots, histograms, 
from tabulate import tabulate
from sklearn.model_selection import train_test_split


ed = pd.read_csv("C:\\Users\\hp\\OneDrive\\python\\python\\working with data sets\\fifa_eda.csv")
print(ed)

print(ed.info())

print("\n value counts \ ")
print(ed['Position'].value_counts())

