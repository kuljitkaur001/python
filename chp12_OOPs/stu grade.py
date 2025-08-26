''' Problem 3: Student Grades
Create a class named Student with the following attributes:

name
marks (list of integers)
Write methods:

add_mark to add a new mark to the marks list.
average to calculate and return the average of the marks.
Create a Student object, add marks using add_mark, and calculate the average.
'''


class stu_grades:
    def __init__(self, list1):
        # self.list = [23,2,21,3,2,3,87,3,53] can not pass list or even any value here 
        self.lis = list1  #acesss everything here , whatever you have wrote above 
        # self.stu_mark = n

    def add_mark(self):
        # self.lis = [3,34,2,4,5,4,45,43,3] can not pass list or even any value here 
        self.lis.append(students_mark)
        print(self.lis)

    def avg(self):
        print(f"the avg of student marks is : {sum(self.lis)/len(self.lis)}")
        

        

object1 = stu_grades([23,3,42,34,3,2,22,3,2,3]) #give every required value here , 
students_mark = int(input("enter you marks : "))
object1.add_mark()
object1.avg()
