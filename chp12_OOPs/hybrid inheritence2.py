# hynrid inheritence containing all four types of inheritence..

class super:
    def __init__(self, a,b):
        self.a = a
        self.b = b 

class sub(super):
    def sum (self):
        print(self.a + self.b) #single inheritence 

class inherit_sub(sub):
    def subtraction(self):
        print(self.a - self.b) #multilevel inheritence 

class inherit_sub_2(sub):
    def multiply(self):
        print(self.a * self.b) #hierarchical inheritecnce

class multiple(inherit_sub,inherit_sub_2):
    def division(self):
        print(self.a/self.b)     #multiple inheritence 

object1 = inherit_sub_2(23,12)
object1.multiply()
object1.sum()
object2 = multiple(23,1)
object2.division()
object2.subtraction()








        