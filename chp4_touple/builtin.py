a=[20,88,176,199,200,1,3]
print(len(a))  #give length of arry
print(max(a))   #gives maximum number in the array 
print(min(a))  # give the minimum number in the array 
print(sum(a)) # giving the sum of whole elements in the arry 
print(sorted(a)) # sort the array 

# all = and (returns false if any one entry is false )
# any = or (returns true if any one entry is ttrue )
 
print("use of any function ")
h = (True, False, True)
print(any(h))
 
print("use of all funciton ")
print(all(h))

# tuple packing 
# tuple unpacking 

 

# neste tuples 
f=((1,2), (3,4), (5,6,7), (0,7))
print(f[2][1])


# touple concatenation 
a=(1,2,3)
b= (4,5,6)
c= a+b
print(c)

# touple repetationm
k=(1,2)*3 # you an print multiple times using any number , i took 3 
print(k)

# touple comparison
t1= (1,2,3)
t2= (1,2,4)
t3=(1,2,3,4)
print(t1<t2) #true becoz 3<4
print(t2<t3) #false becoz 4>3
print(t3<t1) # it comapres elements individuly 



