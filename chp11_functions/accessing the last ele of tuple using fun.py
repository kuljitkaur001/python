# .Access the last element of a tuple (10, 20, 30, 40, 50).
def last_ele(tuple1):
    # tuple1 = input("enter tuple elements by seperating space : ")
    t1 = tuple(map(int,tuple1.split()))
    n = len(t1)
    print(t1)
    print("last element of your tuple is : " , t1[n-1])


tuple2 = input("enter the ele of tuple: ")
last_ele(tuple2)