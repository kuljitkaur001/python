import pandas as pd
df =  pd.read_csv("C:\\Users\\hp\\OneDrive\\python\\python\\Copy of StudentsPerformance(1).xlsx")
print(df)

#describe only works with int vakues 


#to check the unique values in perticular column 

df["gender"].unique() #gender have 2 unique MALE AND FEMLAE 

DELTING A COLUM 

d= df.drop("coumn name", axix = 1 )# axix d;lts the coilumns vertically 

last 20  eentry of data set 

df.tail(20)

checjing the number columns in data 
df.shape

chacking list ame of columns 
df.coloumns

null vlues in columns
df.isnull().sum()

checking unique vals 
df['column name'].unique()


drop only the null and msising values 
df.dropna(inplace = True )



filling vLUES IN PZRTICULZR NULL PART (wroks only with int data )
df["coulmn name "] = g[columns name ].fillna(g["column nama "].mean)


filling null in all coloumns 
F.fillna(0, inplace = True )


line garph of data set .... after removing all trhe null vaulues 


head() returns by 