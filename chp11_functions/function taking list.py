def list_sum(numbers): #function taking one parameter
    total = 0
    for num in numbers: 
        total += num #total = total+num , num = 0 , TOTAL = 0 , total = 0, num = 1, toatl = 0 ,0+1,  total = 1
    return total

my_list = [1, 2, 3, 4, 5]
print("Sum of list:", list_sum(my_list))
