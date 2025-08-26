#.Write a program to check if the string "hello" contains the letter "e".

str = "hello "
print(str.find("e"))


if  str.find("e"):
   print("present")
else:
   print("not present")

# method 2 
# we can find a letter in a string using if else statements 
print(" \n checking using conditionals: ")
text = "hello world "
if "e" in text:
    print("yes , it is present ")
else:
    print("it is not present ")

 