#  Count the number of digits in a given number using a loop.

a = int(input("enter a number : "))
count = 0
# c = len(a)
while(a>0): 
    a = a//10
    count = count+1
print(count)