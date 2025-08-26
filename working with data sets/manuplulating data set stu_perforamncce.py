# https://colab.research.google.com/drive/1HBuD1euf3_ALg5MkhXDdYccBQ105wIP1?usp=sharing#scrollTo=Njt2csuQiw18

#for getting table like grd , do "pip install tabulate "
# this will give tabualte format to yor data set 
#before uploading make sure file is in .csv format 

import pandas as pd #helps to import pandas - , od is shortform pandas , and np is shoprt form of numpy and plt is short form of malplotlib

from tabulate import tabulate

import matplotlib.pyplot as plt #importing matplotlib 

pd.set_option('display.max_columns', None) #for diaplying full coluns  of data set 
pd.set_option('display.width', 1000) #for displaying max width of data set 
pd.set_option('display.expand_frame_repr', False) # used for same as above 
df =  pd.read_csv("C:\\Users\\hp\\OneDrive\\python\\python\\working with data sets\\StudentsPerformance.csv") #df ia a variable, and the path is copy ,  
# print(df) #have to print what we import 


#printing fist 30 rows of data set 
print("\n priting first 30 rows of the data set \n ")
print(tabulate(df.head(30), headers = "keys", tablefmt = "grid")) #.head(30) return the first 30 rows of the data frame in a grid format 

#printing last 30 rows of data set 
print("\n printing last 30 rows of data set \n")
print(tabulate(df.tail(30), headers = "keys", tablefmt = "grid")) #.head(30) return the last 30 rows of the data frame in a grid format 

# checking the number of rows and columns in the data set 
print("\n checking number of columns and number of rows in the data set : ".title())
print(df.shape, "\n")

#cheking name of the availble columns 
print("\n checking name of the aviable column in the data set :  \n ")
print(df.columns) #this will return columns in a list fromat ... 

# to print columsn in the vertical line '
print("-------------------------------------------------")
print(" printing columns in a vertical format \n".title())
for i in df.columns: #this i is iterator 
    print(" ",i, "\n")

print("-----------------------------------------------")
print("to check the data type use by a columns...".title())
print(tabulate(df.info(), headers = "keys", tablefmt = "grid")) # gives a summary of the DataFrame, including:,Number of rows,Column names,Non-null (non-missing) counts per column,Data types (int64, object, etc.),Memory usage 
# print(df.info)

#cheking the statistical values useed in data set like mean median, mode etc
print("checking teh statistical values useed in data set like mean median, mode etc")
print(tabulate(df.describe(), headers = "keys", tablefmt = "grid")) # gives a summary of the DataFrame, including:,Number of rows,Column names,Non-null (non-missing) counts per column,Data types (int64, object, etc.),Memory usage 


#checking unique values a column has 
print("checking uique values a column has ")
# print(tabulate(df["gender"].unique() , tablefmt = "grid"))
print(df["gender"].unique())

#printing in  vertical fromat 
print("\n printing in  vertical fromat : ")
for j in df["gender"].unique():
    print("  ",j)


#checking unique value in another columns 
print("\n checking unique value in anotehr columns : \n")
for l in df["parental level of education"].unique():
    print(" \n ", l)

#this drop is used to dlt a column or row in the data set 
# must store in new varible , whenever deletion occurs need to store in another variable 
# axis = 1 for columns 
# axis = 0 is for rows

# print("\n using drop keyword : ")
# d = df.drop("parental level of education", axis = 1 )
# print(d)

#delting the last colums 

print("\n to dlt last column \ n ")
f = df.iloc[ :, : -1]
print(f)


 
 #---------------------------------------------------------------------------------------#
 #-------------------Mapping----------------------------------------------#
#assiging some other literras to a perticular item
print("\n \n ") 
df["gender"] = df["gender"].map({"male": 1, "female" : 2}) #this simplay chenge the the famle keyword with 2 and male with 1 
print(tabulate(df.head(), headers = "keys", tablefmt = "grid")) 
 
#chekcing unique values of gender after mapping 
print("\n \n checking unique values of gender after mapping :  ")
for m in df["gender"].unique():
    print("\n",m) #female is replaced with 2 and male is repalced wiht 1 


# checking null values 
# print(tabulate(df.isnull(), headers = "keys", tablefmt = "grid"))
print(df.isnull())# return false for not null and true for null values 

print(df.isnull().sum()) #shows is the missing values in every coloumn ....as all the columns have 0 ising values in this data set 

print("\n indexing \n ")
print(df.index) #index shwos the starting point , ending point , and it return one more parameter as "step " means each index is increased by 1 step size . 



# --------------------------------------------------------------------------------------------------------------------------/=
# line graph 

plt.figure(figsize = (12,6) )
plt.plot(df['math score'][ : 50], label = "math score", marker = "o")
# plt.plot(df["reading score"][ : 50], label = "reading score ", marker = "s")
# plt.plot(df["writing score"][ : 50], label = "writing score ", marker = "^" )

plt.title("Performance") #graphs title 
plt.xlabel("students") #x axis tittle
plt.ylabel("score") #yaxis title
plt.legend()  #this is used for showing the graph outliens 
plt.show() #this os used to diaplay graph 

print("\n use of fillna") # fill the not null values 
print(df.fillna(0, inplace = True ))

print("\n checking the null values ")
print(df.isnull().sum())
 

#used ot fill null valus of a perr=ticualr coloumn 
df["test preparation course"] = df["test preparation course"].fillna(df["test preparation course"].mean)

# plt.figure(figsize = (12,6)) #WIDTH IS  12 inchs and height is 6 inches 
# plt.plot(df['math '])