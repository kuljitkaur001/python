# multiple inheritence2

class Input:
    def __init__(self, a, b ):
        self.a = a
        self.b = b 

class formuals:
    def sum(self, x, y):
        print(" \n the addition is = ".title(), self.a+self.b)

    def sub(self, x, y):
        print(" \n the subtraction is = ".title(), self.a-self.b)

    def mul(self, x, y):
        print("\n the multiplication is = ".title(), self.a*self.b)

    def div(self, x, y):
        print(" \n the division is = ".title(), self.a/self.b ,"\n")

class calculations(Input, formuals):
    def show(self):
        self.sum(self.a, self.b)
        self.sub(self.a, self.b)
        self.mul(self.a, self.b)
        self.div(self.a, self.b)



num1= int(input("enter numbr 1: "))
num2= int(input("enter numbr 2: "))
object1 = calculations(num1, num2)
object1.show()
        