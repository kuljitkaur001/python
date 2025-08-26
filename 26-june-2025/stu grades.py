'''Problem 3: Student Grades
Create a class named Student with the following attributes:

name
marks (list of integers)
Write methods:

add_mark to add a new mark to the marks list.
average to calculate and return the average of the marks.
Create a Student object, add marks using add_mark, and calculate the average.
'''
class student:
    def __init__(self, name ):
        self.name = name 
        self.mark_list = [] #list to store values 

    def add_mark(self, mark ):
        self.mark_list.append(mark)

    def avg(self):
        return sum(self.mark_list)/len(self.mark_list)

# afte rfinishing all the method in the class , strt creating the obejct inidietetly 
# so we can create only one object for accessing all the methods in that particular class 

object1 = student("pinki") #creating object 
object1.add_mark(39)
object1.add_mark(32)
object1.add_mark(37)

#printing acgg 
print(object1.name)
print(object1.mark_list)
print("avg is = ",object1.avg())
# print("avg of entered marks is : ", object1.avg())



    
