# write a prpgram to print the table of a given number using for loop 

num = int(input("\n \n which table do you wnat to see : "))

for i in range(1 , 11):
    print(num, "X", i ,"=" , num*i)