# escape sequence charcters starts with backslash , and help to represents the charaters that are not possible to write 
p = "\ni am good girl \n" #\n is help to get in new line
print(p)

i = "hello \t world "
print(i) #\t gives tab space 

h = "hello \\ world"
print(h) #for writing backslash 

y = "hello \' world " #helps to write single quote 
print(y)

f = "hello \" world " #helps to write double quote
print(f)

l = "hello \r world " #only return the string after \r 
print(l)


print("\n \n printing m")
m = "hello \b world "  #dlts one char before \b
print(m)

n = "hello \f world " #seperate the line into words and priitng them into new line 
print(n)

 