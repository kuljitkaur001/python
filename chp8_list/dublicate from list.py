# returning dublicate ele form list 
# retreive length 

list2 = [23,23,1,45,78,34,672,32,23,1,23,1]
list_re=[]
list1=[]
similar=True
for i in range(len(list2)):
    # for p in range (len(list_re)):
        if list2[i] not in list_re:
            list_re.append(list2[i])
        else:
            list1.append(list2[i])
            

print(list1)
     
        

