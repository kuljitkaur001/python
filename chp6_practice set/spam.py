# a spam comment is defined as a text containing the following keywords , "make lot of moeny ", "buy now", "subscribe this ", "click this ", write a program to detect this 
a = input("enter your comment :  ")
comnt1 = "make lot of moeny"
comnt2 = "buy now"
comnt3 = "click this"
comnt4 = "subscribe this"

if(comnt1, comnt2, comnt3, comnt4):
    print("\n \n 1 spam  commmnet detected")
else:
    print("\n no spam detect")

 