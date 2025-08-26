import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.metrics import classification_report

df = pd.read_csv("C:\\Users\\hp\\OneDrive\\python\\python\\working with data sets\\diabetes_dataset.csv")
print(df.head())

x = df.drop(["Outcome"], axis = 1) #giving data to x , that skiping  just last column , but giviing all data beside one column 
y = df["Outcome"] #giving data part to y that is only the lasty column 

x_train, x_test, y_train, y_test = train_test_split(x,y , test_size= 0.2, random_state= 34) #this line is used to divide data in  2 parts , i.e training aprt and testing part
print(x_train)
print(y_train)

clf = RandomForestClassifier(n_estimators= 100)
clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)
print(y_test)


accuracy  = metrics.accuracy_score(y_test, y_pred)
print("accuracy: ", accuracy*100)


print("classifcation report")
print(classification_report(y_test, y_pred))

#Precision ---- 613 --- actual output -- 0
#613 ---- predicted output -- 0 ( Recall --- surety facture )

#precision will check if the predicted output is actual same or not.