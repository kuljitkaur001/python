# Calculate the sum of all even numbers from 1 to n.  

sum = 0
numbers = int(input("enter numbers : "))
for i in range(numbers+1):
    if(i%2 == 0):
        sum=sum+i
print("Sum : ",sum)
