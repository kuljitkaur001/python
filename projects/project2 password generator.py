# password generator .......
# suggested password : 
# length = specified (12)
# capital =  2 lttr 
# numbers = 4
# sepecial chr =  2
# small letters: 4

# sequence  = small , number,special ,  captial 

# process  =  class length , method (4) captial , numbers, lower, special ,  (every method consist of random numbers ...., call every method one by one )


import random 
import string 
class password_generator():
    def __init__(self, length):
        self.length = length

    def Capital(self , capital):
        self.cap = capital
        return capital

    def lower(self, lower):
        self.low = lower
        return lower
        
    def digit(self, number):
        self.num = number
        return number

    def Special(self, special):            
        self.special  = special
        return special


object1 = password_generator(12)

object1.Capital(''.join(random.choices(string.ascii_uppercase, k = 2))) #import function have this parameter ... so we can define our requiremnt .... lie  i need 2 letter of uppercase 
object1.lower(''.join(random.choices(string.ascii_lowercase, k = 4)))
object1.digit(''.join(random.choices(string.digits, k = 4)))
object1.Special(''.join(random.choices(string.punctuation, k = 2)))


password = (
            object1.Capital(''.join(random.choices(string.ascii_uppercase, k = 2))) + 
            object1.digit(''.join(random.choices(string.digits, k = 4)))+
            object1.lower(''.join(random.choices(string.ascii_lowercase, k = 4))) +
            object1.Special(''.join(random.choices(string.punctuation, k = 2)))
            )
print("\n",password,"\n")

