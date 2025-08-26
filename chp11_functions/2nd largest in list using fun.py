# Find the second-largest element in a list without using max() or sorted().
def second_largest(list1):
    n = len(list1)
    for i in range(len(list1)):
        for j in range(i+1, len(list1)):
            if(list1[i]>list1[j]):
                list1[i],list1[j] = list1[j],list1[i]
    print(list1[n-2])




list1 = [23,435,23,456,213]
second_largest(list1)
# max = list[1]
    




