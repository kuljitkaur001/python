# printing even numbers of the list 

L = [1,2,3,4,5,6,7,8]
for i in range(len(L)):
    if(L[i]%2==0):
        print(L[i]) # print the value on that index this will done using []


print("printing even using while ")
i=0
while(i<len(L)) :
    if(L[i]%2==0):
        print(L[i])

    i +=1
