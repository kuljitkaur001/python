# runtime ploymorphodm 
# overriding 

# fastest is the overloading which is complie time polymorphism 

#  run time  poly , function overriding 
class animal :
    def speak(Self): 
        return "some sound "
    
class cat:
    def speak(self): # same function name as previous 
        return "meow"
    

obj = [animal(), cat()]  #single object of both classes .....n
for i in obj: 
    print(i.speak())