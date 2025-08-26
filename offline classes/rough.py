def sum(a,b):
    return a+b
    
number1 = int(input("enter number 1 :"))
number2 = int(input("enter number 2 :"))

print("sum of 2 numbers : ",sum(number1, number2))

sum=lambda a,b:a+b
print(sum(4,7))

# multiply using lambda function 
print("multiply using lambda")
multiply = lambda c,d,e,f:c*d*e*f
[print(multiply(3,2,4,5))]

