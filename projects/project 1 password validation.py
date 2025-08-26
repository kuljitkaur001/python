# password generator .......
# user will input password : 
# length = specified (12)
# capital =  2 lttr 
# numbers = 4
# sepecial chr =  2
# small letters: 4

# algorithm 

# define a format  
# take input from user 

# uses function :
# isdigits() to check number od digits in a string 
# islower() to check number of lower letters in a string 
# isupper() to check number of uppercase letters in string 
# string.punctuation() to check special symbols in a string 


# check if the password is match with the define format or not 
# by checking is there are must be 1 special , 1 uper, 1 lower anf 1 number 
# condition  in 4 ,method ..
# if no specail , no capital , no lower, no number , return one must present 
# if everything accurate, print password is validate 
import string
import sys

class password_generator():
    def __init__(self, length):
        self.length = length
        print("CONDITIONS : \n 1. Password Must Have 2 Uppercase Letters \n 2. Password Must Have 4 Lowercase Letters \n 3. Password Must Have 4 Numbers \n 4. Password Must Have 2 Special Symbols ")
       
    def Capital(self , capital):
        self.cap = capital 
        # input("enter atleast 12 characters : ")
        if len(self.length) <12:
            print("\n ERROR!....  Password Must Contain 12 Characters \n")
            sys.exit()

        else:
            print("\n Contained 12 Characters ")
            
        print("\n Entered Password is : ",enter)    
        # return 
            # sys.exit()

        count1 = 0 
        for i in capital:
            if i.isupper():
                count1 += 1

        if (count1 < 2 ):
            print(" \n ERROR!.... Password Must Have 2 Capital Letters!!")
            # print("password is not validate, you cannot use ".upper())
            
        else:
            print("\n Contained 2 Captials ")

    def Lower(self, lowerr): #for checking lower case letters you need to use islower() funciton 
        self.low = lowerr
        count2 = 0 
        for j in lowerr:
            if j.islower():
                count2+=1
        
        if (count2<4):
            print("\n ERROR!.... Password Must Have 4 Lowercase Letters ")
            # print("password is not validate, you cannot use ".upper())
        else:
            print("\n Contained 4 Lowercase Letters ")
   
    def digit(self, number):
        self.num = number
        count3 = 0 
        for k in number:
            if k.isdigit():
                count3 += 1

        if count3 < 4:
            print("\n ERROR!.....Password Must Have 4 Numbers")
            # print("password is not validate, you cannot use ".upper())
        else:
            print("\n Contained 4 Numbers  ")
    def Special(self, special):            
        self.special  = special
        count4 = 0 
        for l in special:
            if l in string.punctuation:
                count4 += 1

        if (count4<2):
            print("\n ERROR!....Password Must Have 2 Special Characters  \n ")
            print(" \n password is not validate, you cannot use \n ".upper())
        else:
            print("\n Contained 2 Special Characters  \n ")
            print("\n password is  validate, you can use \n ".upper())


        

        
object1 = password_generator("12")
enter = input("\n Enter Password :  ")
object1 = password_generator(enter)
object1.Capital(enter)
object1.Lower(enter)
object1.digit(enter)
object1.Special(enter)
            
