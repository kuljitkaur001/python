# Create a list [1, 2, 3] and print the sum of all its elements.
list10 = [1,2,3,4,5]
print(sum(list10))
print(max(list10))


# using for loop 
# reterive length of list 
# take a vatiable taht initialise sum = 0,,,, sum variable takes value form one by oine form indexes and adds up in thn sum's initial vale , at last the sum wil e stored in the sum variable , so print sum variable 
list11 = [1,2,3,4,45,6] 
sum = 0 
for i in range(len(list11)):
    sum = list11[i]+sum
print(sum)
