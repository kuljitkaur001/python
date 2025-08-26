# shifing zeros at the end 

list1 = [1,0,2,0,3,0,4,0,5,0,5,0,6,0,7,0]
# number = [1,2,3,4,5,6,7,8,9]
num = []
zeros = []
 
for i in list1:
    if (i!=0):
        num.append(i) # putting number from lsit1 and= adding then to "num" lsit 
        # print(num)
        # num = number 
        # list2 = i
    else: 
        zeros.append(i) #adding zeros to zeros list
        # print(zeros)
print(num)
print(zeros)
num.extend(zeros) #adding both lists 
print(num)
# print(list1.append(zeros))



