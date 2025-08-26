# hybrid inheritence 

class super_class():
    def __init__(self, str1):
        self.str = str1

class sub_class1(super_class):
    def show(self):
        print(str3,"how are you  ".title()) #single inheritence 

class sub_class2(sub_class1):
    def display(self):
        print(str3, "where are you livin nowadays  ".title()) #multilevel inheritence 

class sub_class3(sub_class1):
    def tell(self):
        print(str3, "what are you doing  ".title())  #multiple inheritence , hierarchical 


str3 = "prianka"
object1 = sub_class3(str3)
object1.show()

object1.display()  # this display function lies in class 2  has no diret link with subclass 3, this call is not possible , thus eror encountered 


object1.tell()

        

