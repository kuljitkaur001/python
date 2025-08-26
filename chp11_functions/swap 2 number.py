# Swap two numbers x and y using bitwise operators without using a third variable.
# number1 = int(input("enter number1 "))
# number1 = int(input("enter number2 "))
# print()
# x = int(input("enter number 1 :"))
# y = int(input("enter number 2 :"))
def swap(x, y):
    x =  x^y
    y =  x^y
    x =  x^y
    return x,y



x = int(input("enter number 1 : "))
y = int(input("enter number 2 : "))
print("x = ", x , "y = ",y)
print("after swapping ")
x,y = swap(x,y)
print("x = ", x, " y = ", y )