# input() function takes value as a string ...
# if we make sum of the elemnts that are taken by input function  it will not added as sum , instead it concatenates 

a = input("enter number 1 : ") # entered number will assigned to a 
b = input("enter number 2 : ") #entered number will assigned to b 
print("number a is : ", a ) #23
print("number b is : ", b ) #12
print("sum is",a+b) #2312 (concatenates)


r = input("enter anything :  ")
s = input("enter anything : ")
print("value of r = ", r)
print("value of s = ", s)
print(" r + s = ", r+s) 

# if we want that input function convert the values (that are entered by user ) in the int form , (becoz by default input()  function takes values in string form )
# so we use "int" keyword before starting input function . 

g = int(input("enter number 1 : "))
h = int(input("enter number 2 : "))
print("the sum is : " , g + h )


# we can also takes values in float 

i = float(input("enetr any value 1: "))
j = float(input("enter any value 2 :"))
print("the sum is : " , i + j )
print("the multiplication  is : " , i * j )
print("the division is : " , i / j )


