'''
Problem 2: Rectangle Area and Perimeter
Create a class named Rectangle with attributes:

length
width
Write two methods:

area to calculate and return the area of the rectangle.
perimeter to calculate and return the perimeter of the rectangle.
Create an object of the Rectangle class, assign values, and call both methods.

'''

class rectangle:
#init will be there , so it is an by default function..... define basic details in it . and we can access all the values 
    def __init__(s, length , width ):
        s.len = length 
        s.wid = width 

    def area(s):
        return s.len * s.wid 
    
    def perimeter(s):
        return 2*(s.len + s.wid)
    
object1 = rectangle(4, 10)
print(object1.area())
print(object1.perimeter())
