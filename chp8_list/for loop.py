# for loop 
# for loop uses this range function ..this range  function need 2 args, starting val and final val 
# but if we dont add the starting val  or a=only one val i.e  >0 it consider it as the final val and assign 0 as starting val 
# in range function if we write range(1,n), in this n-1 is including , for including the val n , we need to enter  range(1, n+1  )

for i in range (1,6):
    print(i)

# it print upto 9 starting from 0 ... 
print("for loop with one args: ")
for p in range (10):
    print(p)
    
# this range function work also like slicing .. it also includes the step sizd ... as in slicing 
print("for with range function having step size :")
for t in range (1, 100, 4):
    print(t)

# for loop can be used in list , tuple , set 
# for in list 

# steps to use for loop in the list 

# need two variable 
# one for defining list and other one for using in the for loop 
# make a list using sq braces 
# take another variable variable and use it with list
# print the looped variable 
print("for loop in list ")

list1= [1,2,4,4,8644,374532,243,80,6253,29384]

for i in list1:
    print(i)

# for loop with else statement
print("\n \n for loop with else statement ")
list2 = ["prianka","manpreet", "rfd", "jegqkwasd"]
for item in list2:
    print(item)

else:
    print("\n \n done")


# same method cn be used to use the for loop in the tuple 

print("\n for loop in the tuple : ")
tuple1 = (1,34,56,23,6764,42,345,23,23)
for z in tuple1:
    print(z)

# for loop in the string 
#  do not write "range " when you define list tuple or string firstly..... only write"for i in "srting name "
s = "prianka"
for i in s:
    print(i)
     

 


 