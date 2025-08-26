# applied on dataset where we  have a column , which having same values across whole dataset, means never changing its values ... or on quasi constants where 80% of values of colun is same across whole dataset and only 20% is changing... so we drop such cols 

#steps to perform varience threshold 
 #step1 : define an default threshold value
    #step2:find variance of all the input cols .. 
    #step3: drop all the cols having  varience < threshld value 

import pandas as pd 
import numpy as np 
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

df = pd.read_csv("C:\\Users\\hp\\OneDrive\\python\\python\\working with data sets\\human-activity-recognition-with-smartphones\\train.csv")
print(df.shape)

print("before duplicacy data size : ")
x = df.drop("Activity", axis = 1)
y = df["Activity"]

labell = LabelEncoder()
y = labell.fit_transform(y)

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state= 42)
print("\n x_train size :", x_train.shape)
print("\n x_test", x_test.shape)

#removing duplicate values uisng duplicate function 
