# to find the greatest  of 4 numbers 
a = int(input("enter a number : "))
b = int(input("enter number 2 : "))
c = int(input("enter number 3 : "))
d = int(input("enter number 4 : "))

if(a>b and a>c and a>b):
    print("the greatest number is a :", a)
elif(b>c and b>a and b>d):
    print("the greatest number is ",b)
elif(c>d and c>b and c>a):
    print("the greatest number is c :",c)
else:
    print("the greatest number is d: ",d)

print("end of prog : ")

