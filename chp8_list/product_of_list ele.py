# Calculate the product of all elements in a list using a loop.
list2 = [3,2,1,1,5,10]
product = 1
c = len(list2)
for i in range(c):
    product = product*list2[i]
print(product)    