# list , always define in square  braces 
# it is heterogenious .. 

print("\n \n list defining ")
j = [1,[2,4],"k",90.8]
print(j)

# indexing in list
print("\n \n indexing in list ") 
l = [1,[2,4],"k",90.8]
print("\n \n accesing value at index 0 ")
print(l[0])

print("\n \n accesing value at index 1 ")
print(l[1])

# slicing in the list 
print("\n \n accesing from last ")
print(l[-1])

print("accesing form 2nd index to last one ")
print(l[2:-1]) #it will not access the last index by default 



# for adding elemnts in the list , we use built in fucntion 

# entexd()
# append()

# stpes to extend the list 

# apply extend fuction first  
# the print the variable
print("\n \n extend function : ")
a = [12,[1,2],'a', 0.5]
b = [4,5] 
a.extend(b)
print(a)

# apend function 

# steps to append , append adds the values in the list or written form 

# apply fucntion first 
# then print the variable 
print("\n \n append function")
k = [12,[1,2],'a', 0.5]
l = [4,5]
k.append(l)
print(k)

# adding using insert function 
print("\n \n insert function  ")
v = [12,[1,2],'a', 0.5]
v.insert(3,[23,15])
print(v)


# remove function 
print("\n \n remove function , it remmoves the values given in the remove funtion ")
j_ = [12,[1,2],'a', 0.5]
j_.remove(12) 
print(j_)

# pop function 
print("\n \n pop function ")
li_st = [12,[1,2],'a', 0.5]
li_st.pop()
print(li_st) #last values is dlted . whne you do not pass arguents 

# poping from particular index 
print("\n \n sort function ")
l=[3,2,7,5]
l.pop(2)
print(l)


#index 
print("\n \n index function  ")
li_st = [12,[1,2],'a', 0.5]
print(li_st.index("a"))

# sort , works only when the data is of same type 
print("\n \n sort function ")
l=[3,2,7,5]
l.sort()
print(l)

# reverse , works on same data type 
print("\n \n sort function ")
l_=[3,2,7,5]
l_.reverse()
print(l)


# a.clear, it clears whole list in one go 
m = [12,[1,2],'a', 0.5]
print("\n \n clear function ")
m.clear()
print(m)
 

# steps to sort , data should be of same type for sort 
# apply sort function 
# then print the variable 
g = ['banana', 'apple','guava','grapes'] 
g.sort()
print(g)


# copy function 
l = ['banana', 'apple','guava','grapes'] 
g.copy()
print(g)

# list comprehension
 




