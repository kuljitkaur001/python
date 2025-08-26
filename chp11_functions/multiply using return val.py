# multiply using return value  in function 
def multiply(a,b,c):
    return a*b*c

number1 = int(input("\nenter number1 :"))
number2 = int(input("\nenter number2 :"))
number3 = int(input("\nenter number3 :"))

result = multiply(number1, number2, number3)
print(result)