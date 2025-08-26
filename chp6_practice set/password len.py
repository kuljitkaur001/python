# Given a variable password, write a conditional statement to check if the length of password is greater than or equal to 8. If true, print "Strong password", otherwise print "Weak password".

password = input("enter your pasword : ")
c=len(password)
if c==8:
    print("\n strong passsord")
else:
    print("\n weak password ")

