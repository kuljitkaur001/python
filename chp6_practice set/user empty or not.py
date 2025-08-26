# Given a variable username, write a conditional statement to check if username is not empty. If true, print "Username is valid", otherwise print "Username cannot be empty".

username = input("\n enter your name : ")
c=len(username)

if(c==0):
    print("username can not be empty")
else:
    print("valid")