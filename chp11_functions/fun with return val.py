# function with return values 
def add(a, b ): #parameters a and b 
    return a+b # function ends 


print("function with parameters taking value from user : ")

number1 = int(input("\n enter number1 : "))
number2 = int(input("\n enter number2 : "))

result = add(
    number1, number2)
print(result)