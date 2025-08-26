# string is imutable 
# means a strings cannot ba changes once defined 
# you definitely need to define  new string 

a = "prianka" 
b = a[0:4] #prints  values from a to 3rd index , it wil ignore 4th one becoz i cannot access fourth  (last index in the braces will not inclided)
print(b)


c = a[-4:-1]
print(c)
d = a[1:4]
print(d)

# slicing with steps values or skip values

h = "1234567890"
j = h[0:6:3] #it first took strings values from 0 to 6th index , then  it skip 3 values and prints the 4th 
# output: 1,5 (no), its 1,4 , after printing 1. it starts counting from 1 upto 3 units 
print(j)
