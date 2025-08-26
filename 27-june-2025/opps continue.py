class details : 
    def __init__(self, name , age ):
        self.name = name
        self.age = age 
    def student(self):
        print(f" my name is {self.name } and age is {self.age} ")
s = details("jaspreet", 20)
print(s.name)
print(s.age)
s.student()