# Convert a tuple (1, 2, 3, 4, 5) into a list and append 6.

def convert_tuple_to_list(tup):
    tup = tuple(map(int,enter.split()))
    t_  = list(tup)
    t_.append(6)
    print(tup)






enter = input("enter ele of tuple : ")
convert_tuple_to_list(enter)