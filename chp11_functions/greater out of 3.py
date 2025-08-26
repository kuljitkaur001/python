# program to find greatest of three numbers 
def greatest_of_3(a ):
    if(num1 > num2 and num1 > num3):
        print("the greatest number from 3 is : ", num1)
    elif(num2>num1 and num2 >num3):
        print("the greatest number from 3 is : ", num2)
    elif(num3>num1 and num3 > num2):
        print("the greatest number from 3 is : ", num3)
    else:
        print("similar")
    return 


num1 = int(input("enter number1:  "))
num2 = int(input("enter number2:  "))
num3 = int(input("enter number3:  "))
# print("the greatest number from 3 is : ",greatest_of_3(num1, num2, num3))

greatest_of_3(num1)

