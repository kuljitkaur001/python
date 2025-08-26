# .Reverse the list [1, 2, 3, 4, 5] and print the result.
list8 = [1,2,3,4,5]
print(list8[ : : -1])


# using for loop 
list9 = [1,2,3,4,5,6,7]
for i in range(len(list9)-1,-1,-1):
    print(list9[i], end = ' ')