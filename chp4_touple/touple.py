'''A tuple is:

An ordered

Immutable (unchangeable)

Collection of elements.

Defined using parentheses () (but can work without them too)
'''
# touple defined using "()"
print("touple ")
t= (1,2,3,4,5)
print(t)

# accessing the touplle element 
print("\n \n accessing eles from touple ")
print(t[0]) # should have index number 

# slicing 
print("\n \n slicing from touples ")
f= (1,2,3,4,5,5)
print(f[1 : ]) #there should be space . when you are going to keep blnk the slicing spqce 
print(f[4 : ])

# touple function , methods 
# touples have only 2 built in methods 
# 1. count 
# 2. index 

# count 
print("\n \n count in touple ")
f= (1,2,3,4,5,5)
print(f.count(5)) # 5 is 2 times in a touple so output will be : 2

# index value 
# retuens the index of first occurance 
print("\n \n index method ")
print(f.index(5))

# other function that suport touple 

# length function 
print("\n \n gives the length of touple ")
print(len(f))

# max function 
# return the maximum elemnt in a defined touple 

print("\n \n max function ")
print(max(f))

# min 
# returns the minimum function in the touple 
print("\n \n min fucntion ")
print(min(f))

# sum, retunr the sum of all the elemnts in a touple 
print("\n \n sum function ")
print(sum(f))

# sorted 
print("\n \n sorted function ")
print(sorted(f)) #returns sorted list 


# any function 
print("\n \n any function ")
print(any(t))

# all function 
print("\n \n all function ")
print(all(f))

# reversed 
# for reversing a tuple , reversed function is used  inside tuple function 
print("\n \n reversed function ")
print(tuple(reversed(f)))