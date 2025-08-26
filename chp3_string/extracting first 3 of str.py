# .Create a program that extracts the first three characters of the string "PythonProgramming".

str = "pythonprogramming"
print(str[0:3])

# .Create a program that extracts the first three characters of the string "PythonProgramming". using for loop 
str2 = "pythonprogramming" 
extracted = ""

for i in range(3) :
    extracted += str2[i]

print("first 3 letter of string \"pythonprogramming\" is ", extracted)    
