#  15.Check whether a given element exists in a tuple without using in.
# if you wnat to find any thing in the tuple or in list . or you wnt to chekc if this ele us exist then you shoyuld always use th booleran expression 

# initila strt with false ,  use if else stmt with for looop 
 

tuple1 = (23,25,4,53)
c = len(tuple1)
a = 23
found = False
for i in tuple1:
    if(i==23):
        found = True 
        break
if found:
    print("found ")

else:
    print("nope")


# in the form of function 
def exist(ele):
    tuple2 = (324,45,546,65,52365,4354,342,234,342,5,75,53,453,64,432,453,754,463,865,74585,85,65,754,4675,865,754,5,7,456,546,45,657,6,4,56,457,657,57,45,6,457,567,657567,56,7,56,7,657)
    found =False
    for i in tuple2:
        if(i == ele):
            found = True
            break
    if found:
        print(ele, "is exist")
    else:
        print(ele, "is not exist")





ele = int(input("enter the number you wnat to find in the tuple : "))
exist(ele)

