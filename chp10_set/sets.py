
set1 = {1,2,3,4,5,6,}
print(set1)

set2 = set([1,2,3,4,5,6])
print(set2)

# adding values in set 

print("\n ading 7 in set 1")
set1.add(10)
print(set1)

# updating values of set 

print("\n update funtion ")
set1.update([16,15,18])
print("\n updated set ")
print(set1)

# removing values from set
print("\n \n removing 16 using remive fucntion ") 
set1.remove(16)
print(set1)

# remove using discard funtion
print("\n \n remove 10  using discard function ")
set1.remove(10)
print(set1)

# remove using pop function 
# it remives elemnet form starting 
print("\n \n remove using pop fucntion ")
set1.pop()
print(set1)
 
# clear, dtlting whole set in one go 

print("\n \n clear function ")
set1.clear()
print(set1) 

# set operators
# union 
print("\n \n union operator ")
a = {100, 900, 700, 633, 66, 22, 000}
b  = {"a", "h", "r", "t"}
print(a.union(b))


#intersection 
print("\n \n intersection operation ")
a = {100, 900, 700, 633, 66, 22, 000}
b  = {"a", "h", "r", "t", 633, 66, 22, 000}  #retunrs common elemnt only 
print(a.intersection(b))

# differnce 
print("\n \n differnce operation ")
a = {100, 900, 700, 633, 66, 22, 000}
b  = {"a", "h", "r", "t", 633, 66, 22, 000}  
print(a.difference(b))   #only returns from first set entries after comparison 

# symmetric_difference 
print("\n \n symmetric differnce ")
a = {100, 900, 700, 633, 66, 22, 000}
b  = {"a", "h", "r", "t", 633, 66, 22, 000}  
print(a.symmetric_difference(b)) #retutn all the vals that are not common in both of the sets 


# issubset function 
print("\n \n issubset function ")
a = {100, 900, 700, 633, 66, 22, 000}
b  = {"a", "h", "r", "t", 633, 66, 22, 000} 
print(a.issubset(b)) 

# issuperset
print("\n \n issuperset")
a = {100, 900, 700, 633, 66, 22, 000}
b  = {"a", "h", "r", "t", 633, 66, 22, 000} 
print(a.issuperset(b))

# isdisjoint
print("\n \n disjoint ")
a = {100, 900, 700, 633, 66, 22, 000}
b  = {"a", "h", "r", "t", 633, 66, 22, 000} 
print(a.isdisjoint(b)) #return true only when all the entries of both of the set are differnt 

# frozenset 

print("\n \n frozen set ")
z = frozenset('kifewohdwdmnsbd')
print(z)

# can not be added anything in the frozen set nor removed 