import pandas as pd
df =  pd.read_csv("C:\\Users\\hp\\OneDrive\\python\\python\\Copy of StudentsPerformance(1).xlsx")
print(df)

#describe only works with int vakues 


#to check the unique values in perticular column 

df["gender"].unique() #gender have 2 unique MALE AND FEMLAE 

DELTING A COLUM 

d= df.drop("coumn name", axix = 1 )# axix d;lts the coilumns vertically 