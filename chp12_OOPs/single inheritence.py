# parent class 
# need to pass the values on;ly innit
# takes values a and b 
# make other class 
# pass the previous class 
# make 2 methods, sum and subtract 

class calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b 

class operations(calc):
    def sum(self):
        print("addition is ",self.a+self.b) 

    def sub(self):
        print("subtraction  is",self.a - self.b) 
    
num1 = int(input("enter number 1 = "))
num2 = int(input("enter number2 = "))
obect1 = operations(num1,num2)

obect1.sum()
obect1.sub()
        

        

