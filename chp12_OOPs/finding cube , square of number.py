# write a program to find square and  cube of number .......

class calculator:
    def __init__(self, a):
        self.a_ = a
        # self.cube = cube

    def square(self): #this self is taking the variable that are already defined in the previous function 
        print(self.a_*self.a_) #way of accessing 
    
    def cube(self):
        print(self.a_*self.a_*self.a_)

object1 = calculator(12)  #we do not need to pass multikpel values ... , just pass one time and call the functions 
object1.square()
object1.cube()
        