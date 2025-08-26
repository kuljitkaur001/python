# init is a constructor , that do not need to call , but just a need only one parameter, that is self 

class details:
    def __init__(self): # this type of methods known as dunder methods , they do not need to call 
        print("good morning  prianka")


object2 = details() #method be call automatically , just after creating object of class 


# other parameters in the init function 

class student: 
    def __init__(self, name, languge , salary):
        self.name = name
        self.lang = languge
        self.sal = salary


object1 = student("prianka", "java", 37624863698734)
print(object1.name,object1.lang,object1.sal) #call with object (always)
        


