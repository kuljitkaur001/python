class num : #creating class 
    a= 4
    b = 6 
n= num() # creating object of class 
print(n.a) 
#no any class can be run witout --init-- fun 
#it runs in the background 
# function definred in the class knownas __init__
# by default first paramter of trhe method is "self 
# 
# 
class details :
    def __init__(s, name, age): #self is important if you are making method un the class , means if you wnat to pass 2 values , give 3 parameters to def function 
        s.name = name
        s.age = age 
s = details("kuljit kaur", 20) # object will be cretaed as , give new variable , assign it class name with paranethesis
print(s.name) #accessing object 
print(s.age)


# clss with multile method... 
class details :
    def __init__(self, name, age): #self is important if you are making method un the class , means if you wnat to pass 2 values , give 3 parameters to def function 
        self.name = name
        self.age = age 
    def student(self, branch): #this self is accessing the fitst methods elemnts , so now we can use in the 2nd method 
        self.branch = branch
        print(f'my name is {self.name} and age is {self.age} and branch is {self.branch}') # this self wil accesses wll other 


# object will be cretaed as , give new variable , assign it class name with paranthesis
s = details("k", 20)
# print("self only ")
# s.student("cse") #method calling 
s.name="nisha"
print(s.name)
s.student("cse")

#se;f keyword can access all other previous functions paramter 

#changes the paramter values 
