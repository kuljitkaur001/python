#  static method ..... do not need to pass an argument,

# we can make a method as static by adding "@staticmethod"

class details : 
    name = "prianka"

    @staticmethod  #this makes a method as static  , which do not need even self 
    def greet():
        print("good morno ")


object1 = details()
object1.greet()