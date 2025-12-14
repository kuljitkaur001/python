# greeting user using lamba function 

print("greeting using lambda funciton ")
greet = lambda name:print(f"good morning{name}")
greet(" prianka")




def greet(name):
    print(f"good morning {name}")
 
greet("prianka ")


# adding 10 to specific entered number by user 
print("adding 10 in user entered value using lambda funciton ")
# greet = lambda number:print(f"good morning{number}")
add = lambda number : number+10

print(add(7))

# factorial of number

print("\n enter a number ..: ")
def factorial(n):
    if(n==0 ):
        return 1
    elif(n<0):
        print("enter a valid number")
    else:
        return(n*factorial(n-1))
    
number = int(input("enter a number : "))
print(factorial(number))

