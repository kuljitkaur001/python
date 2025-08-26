#find sum of lsit using pyhton 
# in function , for finding the sum , take only one parament 
# initialoze sum 
# find len of list 
# incremnt the sum with index 

# at last return the sum 

# the main list should be added in the main body 
# and print the function with list name 

def sum(a):
    sum = 0 
    for i in range(len(L)): 
        sum = L[i]+sum 
    return sum 
      
L = [88,92,3,17,51]
print(sum(L))



# for largest from list 
# for finding max, consider any number as max elemnt 
# start for 
# take length of list 
# start if 
# compare index with max , remember comapre index with max . 
# store the greater vale in max 
# return max 



def max(a):
    max = L2[0]
    for i in range(len(L2)):
        if(L2[i]>max):
            max = L2[i]
    return max
    
L2 = [88,92,3,17,51]
print(max(L2))


# smallest number in lsit using function 


def small(a):
    min = L3[0]
    for i in range(len(L3)):
        if(L3[i]<min):
            min = L3[i]
    return min 


L3 = [88,92,3,17,51]
print("smallest number in the list ")
print(small(L3))



