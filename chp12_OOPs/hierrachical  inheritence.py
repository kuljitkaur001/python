# hiererachical inheritence , having 2 childs......

class super_class():
    def __init__(self, str1):
        self.str =  str1

class sub_class1(super_class):
    def show(self):
        print("\n",str1,"good morning prianka".title())

class sub_class2(super_class):
    def display(self):
        print("\n",str1,"how are you ".title())


str1= input("\n enter your name : ") 
object1 = sub_class1(str1)
object2 = sub_class2(str1)
object1.show()
object2.display()