# multilevel inheritence 

class one():
    def __init__(self, str1):
        self.str =  str1

class two(one):
    def show(self):
        print("\n",str1,"good morning prianka".title())

class three(two):
    def display(self):
        print("\n",str1,"how are you ".title())


str1= input("\n enter your name : ") 
object1 = three(str1)
object1.show()
object1.display()