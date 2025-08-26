#feture selction with removing duplicate rows . 

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv("C:\\Users\\hp\\OneDrive\\python\\python\\working with data sets\\human-activity-recognition-with-smartphones\\train.csv")
print(df.shape)

x = df.drop("Activity",axis=1)
y = df["Activity"]

labell = LabelEncoder()
y = labell.fit_transform(y)

x_train,x_test, y_train, Y_test = train_test_split(x,y, test_size = 0.2, random_state = 42)
print("training data", x_train.shape)
print("testing data: ", x_test.shape)

print("\n dublicated rows : ", df.duplicated().sum()) #giving number of duplicate rows 
# print("\n dublicated rows : ", df.duplicated()) #giving name of duplicate rows , with "TRUE" val

#dublicated cols 
print("\n dublicated cols : ", df.T.duplicated().sum()) #giving number of duplicate cols 
#since there are 21 duplicaetd cols, lets remove it 

df = df.loc[ : , ~df.T.duplicated()] #removal 
print("after removing duplicacy : ", df.T.duplicated().sum()) #checking 

print("size of data after removing dublicacy : ",df.shape)

x = df.drop("Activity", axis= 1)
y = df["Activity"]

labell = LabelEncoder()
y = labell.fit_transform(y)

x_train, x_test,y_train,  y_test = train_test_split(x,y, test_size= 0.2, random_state= 42)
print("traing data size after removal : ", x_train.shape)
print("traing data size after removal : ", x_test.shape)

log_reg = LogisticRegression(max_iter=10000)
log_reg.fit(x_train, y_train)

y_pred = log_reg.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print("\n test acuracy :", accuracy)






