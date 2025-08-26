'''Goal of RFM
You want to analyze customer behavior:

Who buys most often? (Frequency)

Who spent the most? (Monetary)

Who bought recently? (Recency)'''

import pandas as pd

df = pd.read_csv("C:\\Users\\hp\\OneDrive\\python\\python\\working with data sets\\Online_Retail_.csv", encoding ='ISO-8859-1')
print("size of data set initially ",df.shape)
print("\n data set\n ",df ) #whole data set 

#step 1: data cleaning 

#remove rows does not having customer id 
df = df.dropna(subset= ["CustomerID"])
print("\n shape after removing rows does not having customer id :",df.shape)

#remove canclled orders: (invoice no.satrting with "c")
df = df[~df["InvoiceNo"].astype(str).str.startswith("C")] #df['InvoiceNo'].astype(str), Converts the InvoiceNo column to string type (in case it's numeric or mixed)., .str.startswith('C') 
print("\n size of data after removal of cancelled orders",df.shape)

#removal of rows where cutomers do not but anything i.e = quantity = 0 , and unit price > 0  becoz can not be in negative 
df = df[(df["Quantity"]>0) & df["UnitPrice"]>0] #this line is selecting the rows having quantity value and unit value >0, (both) if anyone is not true , row will be dropped and can not be in selected list 
print("\n size of data after selecting rowa having quanity >0, and unit > 0",df.shape)

# adding a new col which calculating total expenditure by individual . that quanityt*unit price 
    #creating a  new col

# step 2: converting invoicedate to date time . sp that we can ad invoice data time to the timedelta 
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], dayfirst=True) #by dafault pandas hav fomat like month, day , year, which is mismatching with the invoice date that daya, month, year. so we will will give dayfirst = true, measn we are telling to pandas day is coming forts in this format . mconersion done 

#step 3: 
df["TotalPrice"] = df["Quantity"]*df["UnitPrice"]
print("\n data size after adding new col \n ",df)

#step 4: RFM, recency, frequency monetry 

#calculating recency , Purpose: Define a fixed date to calculate "Recency"., according to us, we know recent means what, i week ago, day ago , or a perticuler setled date ago 
    #we should know about latest transation , and the day we are doing RFM analysis  , supppose i have 3 customer they purchase something on 11,23,4 of the same month i will do analysis on the next day to the last purchase , that why we are adding one more day with recent date 
import datetime as dt

reference_date = df["InvoiceDate"].max() + dt.timedelta(days=1)
print("\n reference date : ",reference_date)

#step 5 grouping basis of cutomer id, means we are going to group all similar cutomer ids, no matter hoe much we purchaing , our customer id will be same thought out our whole life, so are going to group similar customer ids, with the product they are by, making total price of all, and calculating the last trancaction time 
rfm = df.groupby("CustomerID").agg({
  "InvoiceDate"  : lambda x:(reference_date -x.max()).days ,#x is the list of purchase date , x.max()gets most recent purchase date, refercne -x.max  , gives the time passed since last purchased, .days= gives you number of days, Last purchase: 2025-07-20-Reference date: 2025-07-31 , → Recency = 11 days
  "InvoiceNo": "nunique", #counts the number of unique invoices., More invoices = more times the customer purchased = Frequency, Invoice numbers: 1001, 1003, 1005 → Frequency = 3
  "TotalPrice": "sum" #Add up all the TotalPrice values for that customer = Monetary, Prices: ₹200, ₹300, ₹250 → Monetary = ₹750
})


#step 6: renamng the cols 

rfm.rename(columns={
    "InvoiceDate" :"Recency",
    "InvoiceNo": "Frequency",
    "TotalPrice": "Monetary"
},inplace =True)

print("\n rfm after renaming : \n \n ".title(), rfm)

#step 7 : data scalling (standarization )

#we are going toapply clustering algorithms , k-means algorithms are distance based so we need to scale all features to the same range eg 0-1 or standard normal distribution  

'''Standardize RFM values
Raw RFM values have very different ranges:

Recency could be from 1 to 400 (days)

Frequency might be 1 to 100

Monetary might be ₹10 to ₹100,000

Use StandardScaler to bring all values to the same scale (mean = 0, std = 1)

'''
from sklearn.preprocessing import StandardScaler

# step 1 : for standarization , we should have a copy of rfm data 

#copying 
rfm_scaled = rfm.copy()

#initializing scaler , basically applying z-score formula,  it calculates the z-score for each value using the formula:z= (x−μ)​/std deviation, It ensures all features are on the same scale, which is crucial for algorithms like KMeans that are sensitive to feature magnitudes.

scaler = StandardScaler()

#fiting and transforming data
rfm_scaled[["Recency", "Frequency","Monetary"]] = scaler.fit_transform(rfm_scaled[["Recency", "Frequency","Monetary"]])
print("\n \n scaled data: \n \n ".title(),rfm_scaled)

# step 7: Clustering with K-Means + Finding Optimal K
  # We’ll use the Elbow Method to find the optimal number of clusters (K), and then apply K-Means to segment the customers.

  #You are using the Elbow Method to decide the best number of customer segments (clusters) to use in KMeans Clustering.

  #KMeans groups customers into clusters based on similarity in their Recency, Frequency, and Monetary behavior (after scaling).

  #How many clusters (K) should you use? That’s what the Elbow Method helps you find.

#To find out how many customer segments (K) you should create from your RFM data.

# using KMeans for clustering

#And matplotlib to draw the Elbow curve
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


#try k values from 1 to 10 
#prepare empty list first

sse = [] #"sse" sum of squred errors , it shows how tightly points are gruoped in a cluster , lower sse = bettwe sse 

#try k values from 1 to 10 
for k in range(1,11):
    kmeans = KMeans(n_clusters = k, random_state = 42)
    kmeans.fit(rfm_scaled) # Run clustering on scaled RFM data
    sse.append(kmeans.inertia_) # Measures how far the data points are from their cluster centers,  Save the SSE result for that K

#ploting the elbow corner 

plt.figure(figsize = (8,5))
plt.plot(range(1,11),sse, marker = "o")
plt.xlabel("number of clusters (k)")
plt.ylabel ("SSE(intertia)")
plt.title("elbow method for optional k ")
plt.grid(True)
plt.savefig("elbow_plot.png")
plt.show()


#aplying kmeans with chosen k (i.e = 2)
# Apply KMeans with optimal K (change to your chosen number)
optimal_k = 4
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
rfm_scaled['Cluster'] = kmeans.fit_predict(rfm_scaled)

# Also add cluster label to original (unscaled) RFM
rfm['Cluster'] = rfm_scaled['Cluster']

# View the segmented customers
print(rfm)


# Count of Customers in Each Cluster
import seaborn as sns

sns.countplot(data = rfm, x = "Cluster")
plt.title("number of customer in each cluster ")
plt.xlabel("Cluster")
plt.ylabel("count")
plt.show()

 

# Average RFM Values per Cluster
cluster_summary= rfm.groupby("Cluster").mean(numeric_only = True)
print(cluster_summary)

# 2D Scatter Plot of Clusters (Using Recency & Frequency)

#cluster labels 
## Map cluster numbers to descriptive labels
segment_labels = {
    0:"low-engaged",
    1:"churned",
    2:"vip",
    3:"Regulars"
    
}

rfm["segments"] = rfm["Cluster"].map(segment_labels)

plt.figure(figsize=(8,6))
sns.scatterplot(
    data = rfm,
    x = "Recency",
    y = "Frequency",
    hue = "segments",
    palette="Set2",
    s=100
)
print("customer segmenation (recency vs Frequency)".title())
plt.show()

#country wise customer distribution 
customer_country = df[["CustomerID", "Country"]].drop_duplicates()
top_countries = customer_country["Country"].value_counts() 
plt.figure(figsize=(18,6))
top_countries.plot(kind = "bar", color = "green", edgecolor = "black")
plt.title("Top 10 Countries by Number of Customers", fontsize = 14, fontweight = "bold")
plt.xlabel ("country ", fontsize = 12)
plt.ylabel ("number of customers per country ", fontsize = 12)
plt.xticks(rotation = 90, fontsize = 8)
plt.yticks(fontsize = 10)
plt.grid(axis = "y", linestyle = "--", alpha = 0.7)
plt.tight_layout() # avoids label overlap
plt.show()

# 4. Time Series of Orders

#Use InvoiceDate to show:

print("\n \n monthly sold sold quantities ")
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"]) #pd.to_datetime() converts it into a Pandas DateTime object.

#Extract Month as a Period
df["month"]= df["InvoiceDate"].dt.to_period("M")

#Group Data by Month & Sum Quantities
monthly_sales = df.groupby("month")["Quantity"].sum()

#Plot Monthly Sales
plt.figure(figsize=(18,6))
monthly_sales.plot(kind = "line", title = "monthly sales volume ") #kind='line' → creates a line chart., On the x-axis → months (2025-01, 2025-02, …).,On the y-axis → total quantity sold in that month.

plt.xlabel("Month")
plt.ylabel("Total Quantity sold")
plt.grid(True)
plt.show()


# Export Final Clustered Customers

rfm.to_csv("clustered_customer.csv", index = False)
print("file saved sucessfully ")

df = rfm #inspection code directly on rfm instead of reading clustered_customer.csv again., code for reading the exporting file again 

print("\n acheived data set size :".title(), df.shape)#.shape returns (rows, columns).
print("\n coloumn name : ".title(), df.columns.tolist())#.tolist() converts them from an index object to a normal Python list.

#checing data types 
print("\n data types of columns ".title(), df.dtypes) #.dtypes shows the type of each column (e.g., int64, float64, object for text).

#checking frist 5 values of data set
print("\n preview of data : ".title(), df.head()) #.head() shows the first 5 rows by default.

#range and outliers 
print("\n summary statictics :".title(), df.describe()) #.describe() gives mean, median, min, max, std dev, and quartiles for numeric columns.

#See unique clusters
print("\n unique clusters : ", df["Cluster"].unique())

#unique segment labels 
print("\n unique segments labels : ".title(), df["segments"])



