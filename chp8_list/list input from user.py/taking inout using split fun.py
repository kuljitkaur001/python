# method one of taking input list form user 
# uisng input and split function 

# we need 2 var ,
# one for taking input from user 
# one for printing the list, , which contains split  function  , remember we can only print the 2nd variabel , where we have use the split function variable... 

#  that split function can only take values in the form  of string, 

# so need to agian converting in the form  of int 

lis = input("enter numbers seperated by space :")
my_list = lis.split() # adding up numbers in the form of list 
print(type(my_list[1])) #showing tyhe type of values 
print(my_list)

#using map function


my_list = list(map(int, input("Enter numbers: ").split()))
print(my_list)


 
