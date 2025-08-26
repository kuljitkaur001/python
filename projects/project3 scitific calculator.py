# project 3, scietific calculator ..... 

# used funciton , .tittle(), used ot make cpaitalize the firts letter of every word in the particular string 

# simple calculator 
# class , 4 methods, sum, mul, division, sub
# program will ask from user , which operationdo they want to perform .....
# only then the fucnction will be called 

class calcualator:
    def __init__(self, a , b ):
        self.a = a
        self.b = b 
    
    def sum(self):
        print(f"\n  {self.a} + {self.b} = ",self.a+self.b)

    def subtract(self):
        print(f" \n {self.a} - {self.b}  = ", self.a-self.b)
    
    def multiply(self):
        print(f" \n {self.a} * {self.b}  = ",self.a *self.b)

    def division(self):
        print(f" \n {self.a} / {self.b}  = ", self.a/self.b)

    def modulus(self):
        print(f" \n {self.a} % {self.b}  = ", self.a%self.b)

    def square(self, x):
        print(f"{self.a} * {self.a} = ", x*x)
        
operation = input(" \n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division \n 5.modulus \n 6. sqaure \n which operation do you want to perform , Enter Number From Given Choices : ".title())
# print("")
if operation == "1":
    print("\n You Have Choose Addition ".title())

elif operation == "2":
    print("\n You Have Choosen Subtraction".title())
 
elif(operation == "3"):
    print("\n you have choose multiplication".title())

elif (operation == "4"):
    print("\n you have choosen division ".title())
    
elif(operation == "5"):
    print("\n you have choosen modulus operation ".title())

elif(operation == "6"):
    print("\n you have choosen square operation ".title())

numnber1 = int(input("\n enter number 1 : ".title()))
numnber2 = int(input("\n enter number 2 : ".title()))
object1 = calcualator(numnber1, numnber2)

if (operation == "1"):
    object1.sum()
elif(operation == "2"):
    object1.subtract()

elif (operation == '3'):
    object1.multiply()

elif(operation=="4"):
    object1.division()

elif(operation == "5"):
    object1.modulus()

elif(operation == "6"):
    num = int(input("enter number".title()))
    object1.square(num)