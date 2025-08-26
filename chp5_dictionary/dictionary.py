#  dictionary is an unordered, changeable, and indexed collection of key-value pairs.
# Each key must be unique, and it is used to access its corresponding value.
student = {
    "name" : "prianka",
    "age" : " 21",
    "course" : "b.tech"
}

# dictionary using dict function 
print("\n dict vals ")
person = dict(clas = "b.tech", age_ = "45", city = "ludhiana" )
print(person )


# accessing the values from dictionary 
print("studnet course ")
print(student[ "course"])
print() #for space 

print("\nstu age")
print(student["age" ])

print("\n stu name ")
print(student["name" ])

# accesing only keys from dictionary 
print("\n stu keys ")
print(student.keys()) 

# accesing only values
print("\n stu vals ")
print(student.values())

# accessing needed elements from dicttionary 
print("\n accessing required item form dictionary ")
print(list(student.items())[1][1])

# accessing the dictionary elemnts using get function 
print("\n get function ")
print(student.get("course"))
 
# adding new value in the dictionary 
print("\n adding new value in student dicionary : ")
student["city"] = "amritsar"
print("\n updated dictionary = ", student)
# print(student)

# changing the value in dictionary 
print("\n updating single val in dictionary ")
student["age"] = 34
print(student) # age chnages form 21 to 34 
# print(student.update())
# or
# student.update()

# removing elements from dictionary 
# student.clear() #remove all elements in one go 
# print(student)

# class is the keyword , cannot be used directly 
stu_class= {
    "name" : "mnpreet",
    "roll no " : " 12",
    "course" : "b.tech"
  } 
print("\n \n poping roll no ")
stu_class.pop("roll no ")
print(stu_class) #age dlts 

# removing elements uding del 
town = {
    "name" : "mnpreet",
    "roll_no" : " 12",
    "course" : "b.tech"
  }
del town["roll_no"]
print("\n \n roll no dltd ")
print(town)

print("\n \n pop item function  ")
town.popitem() # always write function first , then print 
print(town)
 

# del fucntion 
# d.clear 
# popitem()
# d.keys 
# d.values
# list(d.item()[1][1]) , idex vals 
# d.gte(key)
