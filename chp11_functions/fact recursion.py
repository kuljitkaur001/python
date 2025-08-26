# recursion , rescursion calls it self again and again

# reverse a funciton using
# firsly add base case using if  , becpoz fact(1) = 1, and fact(0) = 1
# return n*n-1

def factorial(n): #becoz , factorial will be of a single numbers only , at last only one val comes as out put 
    if(n == 1 or n == 0 ):
        return 1 
    return n * factorial(n-1)

n = int(input("enter a number to find the factorial:  "))
print("factorial of your number is : ", factorial(n))


def fact_(n):
    if(n == 1 or n == 0 ):
        return 1
    return n*factorial(n-1)

num = int(input("\n enter a number you wnat to take factotrial of : "))
print("the factorial of", num, "is ", fact_(num))

