''' Problem 2: Rectangle Area and Perimeter , Create a class named Rectangle with attributes:

length
width
Write two methods:

area to calculate and return the area of the rectangle.
perimeter to calculate and return the perimeter of the rectangle.
Create an object of the Rectangle class, assign values, and call both methods.
'''


class rectangle :
    def __init__(self, width, length ):
        self.wid = width
        self.len = length

    def area(self):
        print(f"area of rectangle is {self.len * self.wid}")

    def perimeter(self):
        print(f"the perimater of rectangle is {2*(self.len + self.wid)}")

object1 = rectangle(2, 4)
object1.area()
object1.perimeter()