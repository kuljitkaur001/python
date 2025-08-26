# .Concatenate two tuples (1, 2, 3) and (4, 5, 6), and determine the output.
def concatenate(t1, t2 ):
    t1 = tuple(map(int, tuple1.split()))
    t2 = tuple(map(int, tuple2.split()))

    print(t1+t2)
    


tuple1 = input("enter the ele of tuple : ")
tuple2 = input("enter the ele of tuple : ")
concatenate(tuple1, tuple2)
# tuple2 = (11,21,51,61)
# print(tuple1 + tuple2)



