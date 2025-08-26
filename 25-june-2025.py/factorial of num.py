def factorial(number):
    if(number == 1 or number == 0 ):
        return 1
     
    return number *factorial(number-1)  #  5*4*3*2*1, 5*(5-1)!
    

fact = int(input("enter a nunber you want to see the factorial : "))
print(factorial(fact))