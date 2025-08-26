# # .Replace the second element of a list [5, 15, 25, 35] with 20.
# list do not have replace function ...., os we have to do it manually .. by accessing the firts index 
# def replacing(l):
#     c = l.replace("15", "20")
#     return c


# list1 = [5,15,25,35]
# print("after replacing : " , replacing(list1))


def replacing(list2):
    user_list = []
    list2[1]= 20
    return list2


print("the list after replacing is: ", replacing([2,23,34,4,5,56465,6,4,4,2,432,234,2,54,6,]))
# list1 = [12,34,5,21,4,2]
# for i in list1:
# list1[1] = 20 
# print(list1)
