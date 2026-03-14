#It is commonly used to initialize variables (attributes) of the class.
# The first parameter is usually self, which refers to the current object.
# self → refers to the object
# self.name, → variables stored inside the object

class student:
    def __init__(self, name ):
        self.name = name 
    
    
class teacher :
    def __init__(self, name):
        self.name = name 

    def teach(self, student):
        print(self.name, "teaches", student.name)


s1 = student("aman")
t1 = teacher("singh")

t1.teach(s1)