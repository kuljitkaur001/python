'''Problem 5: Circle Operations
Create a class named Circle with:

radius
Write methods:

area to calculate the area of the circle.
circumference to calculate the circumference of the circle.
Create a Circle object, assign a radius, and call both methods.
'''

class circle:
    def __init__(self, radius):
        self.radius = radius 

    def area(self):
        return 3.14 *( self.radius * self.radius)
    
    def circumference(self):
        return 2*3.114* self.radius
    
object1 = circle(12)
print(object1.area())

print(object1.circumference())

        
