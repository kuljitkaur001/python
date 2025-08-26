# Write a program to find the smallest number in a list using a loop.  

numbers = [23,12,45,1,11]
c = len(numbers)
smallest_number =numbers[0]
for i in range(c):
    if(numbers[i]<smallest_number):
        smallest_number = numbers[i]
print(smallest_number)
