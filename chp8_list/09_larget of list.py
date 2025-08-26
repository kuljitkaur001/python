# Find the largest number in a list using a loop.  
# firstly take length of list, using new variable 
# take a variable about what you want as i want largest number 
# use for loop 

numbers = [1,2,3,4,5,6,7,8]
c = len(numbers)
largest_num = numbers[0]
for i in range(c):
    if(numbers[i]>largest_num):
        largest_num=numbers[i]
print(largest_num)