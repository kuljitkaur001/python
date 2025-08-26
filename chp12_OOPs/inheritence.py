# inheritence
class employee():
    def __init__(self, name, id ):
        self.name = name
        self.id = id 
    
    def show(self):
        print(f"the name is {self.name} and id is {self.id}")



class programmer(employee ): #this employee is the previous class name , we inherit previous class like this 
    def showlang(self):
        print("the default lang is python ")
        

# object1  = employee("rohan", 20)
# object1.show()

object2  = programmer("rohan", 20) #this object is belongs to newer class and we can access the previous classes mthod using newer class objects 
object2.show()
object2.showlang() 
