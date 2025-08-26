# Modify a list inside a tuple to change an element without replacing the tuple.
def modify(tupple):
    tupple = list(map(int, tupple.split()))
    tupple.append(6)
    print(tupple)
    c = len(tupple)

    
    # tuple1 = (1,2, [23,1,3,4])
    # tuple1[2][1] = 12


tupple1 = input("enter element for tuple containing laist seperating by space : ") 
modify(tupple1)
# tuple1 = (1,2, [23,1,3,4])
# tuple1[2][1] = 12
# print(tuple1)
