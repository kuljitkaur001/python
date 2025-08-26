'''Problem 7: Calculator
Create a class Calculator with methods:

add(a, b)
subtract(a, b)
multiply(a, b)
divide(a, b) (handle division by zero)
Create an object and call these methods with sample inputs.
'''

class calculator : 
    def __init__(self, a,b ):
        self.a = a
        self.b = b 
    
    def add(self):
        return self.a + self.b
    
    def divide(self):
        if (self.a ==  0 or self.b == 0 ):
            print("division can not be possible ")
        else: 
            return self.a / self.b
    
    def multiply(self):
        return self.a*self.b
    
    def subtract(self):
        return self.a - self.b        


# operation = print("enter operation : ")
number1 = int(input("enter number1 : "))
number2 = int(input("enter number2 : "))
object1 = calculator(number1,number2)
print("the sum is : ", object1.add())
print("the multiply  is : ", object1.multiply())
print("the subtraction is : ", object1.subtract())
print("the divide is : ", object1.divide())
# print("the sum is : ", object1.add())
