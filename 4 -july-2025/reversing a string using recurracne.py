# reversing a string using recursion 
# hello = olleh
def rev_str_using_rec(str1):
    if len(str1) == 0 :
        return str1
    
    else : 
        return rev_str_using_rec(str1[1:]) + str1[0]



str1 = input("\n enter a sting :".title())
print(rev_str_using_rec(str1))


# differnt thing 
str2 = "hello"
str3 = str2[1: ] 
print(str3)

