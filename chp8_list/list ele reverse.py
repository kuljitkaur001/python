# printing the elements of list in reverse order 

# for reversing we need 3 parameters in the range function -1,-1,-1
# 1. -1 is for subtracting the last entery index .. becoz we have indexes uptp 9 ,but length is 9 , so  9-1 = 8 

# 2nd -1 is for accessing the val at index 0 , becoz if we write 0 ,  it access only the value upto 1 index , not upto 0 

# 3. the -1 is for reverse order . 


List1 = [12,23,21,34,1,2,67,676,7]
for i in range(len(List1)-1,-1,-1):
    print(List1[i])


