# more than 2 base classes 
# having onoy one inheriteed class . 

class calculator :
    def __init__(self, a, b ):
        self.a = a
        self.b = b 

class claculator_2:
    def sum(self):
        print("the addition is = ".title(), self.a+self.b)


class calculator_3(calculator,claculator_2):
    def subtract(self):
        print("the subtraction is = ".title(), self.a-self.b)



number1 = int(input("enter number 1: "))
number2 = int(input("enter number 2: "))
object1 = calculator_3(number1, number2)

object1.sum()
object1.subtract()
        