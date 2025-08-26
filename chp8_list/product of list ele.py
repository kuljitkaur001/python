# product of list elemnt 
#take the length of the list in the case of sum or product o flist elements 
# assign product = 1 and sum = 0 (always )
# store the multiplication or sum of lisy indexed values in product variable 

# just outside the for loop , print product , becoz we are saving all the values in product variables  

print(" \n product of list elements ")
product = 1 
list1 = [1,2,3,4,5,6,7,8,9]
for i in range(len(list1)):
    product = list1[i]*product

print(product)

