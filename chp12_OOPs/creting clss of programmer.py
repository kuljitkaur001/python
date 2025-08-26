# crete a class of  a programmer for storing information of programers working at microsoft

class programer:
    def __init__(self, name , salary , jobrole, language):
        self.name = name 
        self.sal = salary 
        self.jobrole = jobrole 
        self.lang = language

object1 =  programer("prinaka", 876834935963, "data sceintist", "pyhon") #always pass the arguments in while creting the object of classs
print(object1.name, object1.sal, object1.jobrole, object1.lang)