# .Write a program to count how many times the value 3 appears in the tuple (1, 3, 3, 5, 3).

# whebever we have to find the occurance of ele, take an var count .... and incremnt it 
tuple8 = (1,3,3,5,3)
count = 0 
for i in tuple8:
    if (i == 3):
        count = count+1
print("the count of 3 is ",count)