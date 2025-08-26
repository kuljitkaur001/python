# You have a variable marks. Write a conditional statement to check if marks are greater than 75. If true, print "Distinction", if marks are between 50 and 75, print "Pass", otherwise print "Fail".

marks = int(input("enter you marks : "))
if(marks>=75):
    print("distinction")
elif(marks>=50 & marks<=75):
    print("pass")
else:
    print("fail")