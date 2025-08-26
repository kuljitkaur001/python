# create a class with class attribute, create an object form it and set a directly using object.a=0, does this change the class attribute 



class attribute:
    a = 23

object1 = attribute()
object1.a = 34
print(object1.a)
print(attribute.a)

# ans = no, becoz an instances of object is created when we change class attribute , an instance of object is created , otherwise class attribute can not be changed 