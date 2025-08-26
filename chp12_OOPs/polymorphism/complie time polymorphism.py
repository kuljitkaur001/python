# compile time polymorphism ... 

# banking system ...... program showing the polymorphism 

class details:
    def __init__(self, a):
        self.a= a 

    def calculator (self, b):
        self.b = b
        print(self.a +self.b)
    
    # def show(self):
    #     print()

object1 = details(12)
object1.calculator(3)  #the values are passing differntly .... so this is showing overloading ...
        