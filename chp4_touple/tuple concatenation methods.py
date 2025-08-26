# concatenation tuples (methods )

# method 1
t1 = (1,3,4,5)
t2 = (12,32,42,52)
print("concatenation using \"+\" =  ",t1+t2)


# method 2 using tuple unpacking  operator(*)
# but this methods does not seperate the tuple eles with comma 
t3 = (1,3,4,5)
t4 = (12,32,42,52)
print("using tuple unpacking  operator (*): ", *t3, *t4)


# uisng loop 

t5 = (1,3,4,5)
t6 = (12,32,42,52)
for i