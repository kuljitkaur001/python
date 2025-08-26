#feature seletion 

from sklearn.datasets import load_iris #.datasets contains popular practicing data sets for ml as load_iris
from sklearn.feature_selection import SelectKBest, f_classif #SelectKBest selects the top k highest-scoring features based on a scoring function like f_classif., f_classif is a statistical test that scores features based on how well they separate 

# for feature scalling 
from sklearn.preprocessing import StandardScaler
import numpy as np 



#laoding the sample data 
data = load_iris()
x = data.data #  # input features  # independent variables, means it contains actuall data , like this dataset have 154 rows and total 4 coul, so x conatins all 


y = data.target ## target class   # dependent variable
print("\n data ", data) #the output shows 2d array , where each inner list is represent to a flower and th enumbers are measuremnets of the flower sample  , 

#Sepal length = 5.1 cm

# Sepal width = 3.5 cm

# Petal length = 1.4 cm

# Petal width = 0.2 cm

# Each row = one flower.

#viewing the data set 
print("feature data (x): \n ",x)

#viweing 5 coloumn only 
print("feature data upto 5 cols : ", x[ : 5])

#showinf feature names 
print("feature names : ", data.feature_names)

#showing the target names : 
print("\n taret names : ", data.target_names)

#showing target labels 
print("target labels : ", data.target) #this will show output as 0 ,1,2 where 0 refer to setosa , 1  = versicolar, 2 = virginca , means which row belongs to which species . 

#selecting 2 K best features 

# This code selects the top 3 most important input features that help predict the flower species (target y) and prints the reduced dataset x_new
selector = SelectKBest(score_func = f_classif, k=3) #This creates a feature selector that will choose the top 3 features., : Uses ANOVA F-test to measure how important each feature is., k=3: Keep only the top 3 features based on their F-score

x_new = selector.fit_transform(x,y) #This applies the selector to your data., fit: Calculates F-scores between each feature in x and target y., transform: Keeps only the best k=3 features., x_new: Now contains a reduced version of your data — only the top 3 features per sample.
print("\n printing x_new", x_new)

#shape before doing feature selction , 
print("original shape : ", x.shape), #150 rows and 4 cols 

#shape after feature selection . 
print("shape (size ) after feature selection : ", x_new.shape) #only have 3 best columns and 150 rows 


#---------------------feature scalling -------------------------------
arr = np.array([[1,2],[3,4],[5,6],[7,8]]) #i have cretwd this numpy array  , having shape (4 rows* 2 cols)
scaler = StandardScaler() #Creates a StandardScaler object from sklearn.preprocessing.Mean = 0 , Standard deviation = 1 , z = (x-mean)/standard deviation
x= scaler.fit_transform(arr) #fit calculates the mean and std of each column., transform scales each value using the formula above.
print(x)

# Bias( error ) --   difference between actual data point and predicted data point
# variance -- difference between 2 actual data points