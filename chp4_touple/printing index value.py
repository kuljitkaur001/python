# Create a tuple (5, 10, 15) and print the index of the value 10.
# for checking index value , firslty reterive the len of tuple, lsit and string 
# print iterator in this type of cases 
tuple7 = (5,10,25)
index = 0 
for i in range(len(tuple7)):
    if (tuple7[i]==10):
        print(i)
        break
    
