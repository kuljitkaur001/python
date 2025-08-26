# tuple eles input by user 

# method 1  uisng  tuple() function , map() and input function()

tuple1 = input("enter the ele of tuple : ")
t = tuple(map(int,tuple1.split()))
print(t)


# tuple of strings 
tuple2 = input("enter the ele of tuple : ")
t1 = tuple(tuple2.split())
print(t1)
