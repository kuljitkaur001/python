# finding the maximum element in the list v=uisng for loop 
# consider any indesxed ele as max .. 

# take length first ...  

L = [23,12,5,62,3,789,23]

max = L[0]
for i in L:
    if(i>max):
        max = i 

print(max)

# take length of list ele first 


print("taking length first : ")
L = [23,12,5,62,3,789,23]
c = len(L)
max = L[0]
for i in range(c):
    if(L[i]>max):
        max = L[i] 

print(max)



