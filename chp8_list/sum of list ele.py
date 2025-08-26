# sum of list eles 

# got the length of list first of all 
# always print will be in the outside of the for loop ..... whenever we are printing sum 


sum = 0 
L = [1,2,3,4,5,6,7,8]
for i in range(len(L)): 
    sum = L[i]+sum
    
print(sum)

print("\n sum using while :")
sum = 0 
L = [1,2,3,4,5,6,7,8]
for i in range(len(L)): 
    sum = L[i]+sum
    
print(sum) 



# sum = 1 
# L = [1,2,3,4,5,6,7,8]
# for i in range(len(L)):
#     print(L[i]+sum )