def greatest_of_3(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
number1  = int(input("enter number 1 "))
number2  = int(input("enter number 2 "))
number3  = int(input("enter number 3 "))
print(greatest_of_3(number1, number2, number3))