import numpy as np 

#creting numpy array 

#function 1:  np.array()
a = np.array([1,2,3]) #pass list in array function 
print("\n a :",a)
print(" type of a : ".title(), type(a))

#2d numpy array 

b = np.array([[1,2,3],[2,3,4]])
print("\n 2d array b :\n",b)
print(" type of b : ".title(), type(b))

#3d array , gives three sq braces 

c = np.array([[[1,2],[1,2],[1,2]]])
print("\n 3d array\n ",c)

#creting a float array 

d = np.array([1,2,3],dtype=float)#dtypr changes the datatype from interger t flaot or any other 
print("float array : ", d)

#dtype 
d = np.array([1,2,3],dtype=bool)#dtypr changes the datatype from interger t flaot or any other 
print("float array : ", d)

d = np.array([1,2,3],dtype=str)#dtypr changes the datatype from interger t flaot or any other 
print("float array : ", d)

d = np.array([1,2,3],dtype=complex)#dtypr changes the datatype from interger t flaot or any other 
print("float array : ", d)

#function 2: np.arange() 
#this arange is juat same as for loop range function , we give range and it print in array format 

e  = np.arange(1,11)
print(e)

e  = np.arange(1,11,2) #2 is the step size 
print(e)
