class student :
    def __init__(self, name ):
        self.name = name 

class dept:
    def __init__(self, student):
        self.student = student

s1 = student("aman")
d1 = dept(s1)

print(d1.student.name)
        
        