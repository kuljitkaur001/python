lis = []
print("enter 5 numbers : ")

for i in range(5):
    user_input  = input(f"enter {i+1} : ")

    lis.append(int(user_input))
print("lsit", lis)
print(max(lis))
print(sum(lis))


