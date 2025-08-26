#a machine learning classification model using Logistic Regression that achieves 90% accuracy on test data
#feature selection on human-activity-recognition-with-smartphones.

#prediction model 

import pandas as pd 
import numpy as np

#let see dataset 
df = pd.read_csv("C:\\Users\\hp\\OneDrive\\python\\python\\working with data sets\\human-activity-recognition-with-smartphones\\train.csv").drop(columns="subject")

# checking the velue of last columns 
#value count gievs us values a prticular col have 
print(df["Activity"].value_counts())

print("\n the size of whole data  ".title(),df.shape)

#steps ot feature selection 
#step 1: find the shape , the output col, first 5 rows, 
 # step 2: divide teh data set in 2 parts , training data and testing data 
 # step 3: apply feature selection on training data
    # 20 percent data is for test , 80 % is for training 
     # for diving data we need 2 var , x for input, y for output 

x = df.drop("Activity", axis = 1) #df is compltely here, but with droping activity col 
y = df["Activity"] 
  
#we have output col: activity , which in string , we need ot convert it in 01 format . so 1st activity mread as = 0, 2nd = 2, 3rd = 3 ... so on 
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#step 3: encode the target data(output data means data storeed in y ) , if output data is in string format 
   #Many ML models (like Logistic Regression) require numeric values.
lebell = LabelEncoder() 
y = lebell.fit_transform(y) #fir read unique label , tranform , turn each unique label with numeric val

 # step 4 :  divind data into training and tetting part 
x_train , x_test , y_train , y_test = train_test_split(x, y , test_size = 0.2, random_state = 42)
print("\n training data size".title(),x_train.shape)
print("\n testing data size".title(),x_test.shape)
#  the accuracy of data 

#accuracy of the data 
 #we have to apply logistic regressio onn 562 cols first , so that we have accuracy of data set 
    #for applying logostic regression import sykit learn libraries 

    #applying logistic regression 

log_reg = LogisticRegression(max_iter = 1000) #Maximum number of tries (steps) the model will take to find the best answer., max_iter=1000	"Try up to 1000 times to get the best result."

# You're telling the Logistic Regression model:

# “Learn from this data training  of data , Fits (trains) the model on the training data.
log_reg.fit(x_train, y_train) #Hey model, here's the data (x_train) and the correct answers (y_train). Learn the pattern."
print("\n ----------------traing compaltes-----------------, predicts begins ")
#prediction , Uses the trained model to predict activity on unseen test data., prediction will always apply on the test data 
y_pred = log_reg.predict(x_test) #Your model is trained and ready to use!

#printing the accuray score , We use test data to check performance:, Accuracy just needs the actual vs predicted labels — both are in y_test and y_pred.

 #accuracy do not need the training data,  accuracy = Number of correct predictions/total predictions , total prediction = Y_pred and correct predictyion = Y+test, so always accuracty must have y_test, and y_pred


accuracy = accuracy_score(y_test, y_pred)
print("\n tests accuracy: ", accuracy)


#model done _______







