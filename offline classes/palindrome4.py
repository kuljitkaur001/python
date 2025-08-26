def plaindrome_check(string1):

    string_rev = string1[ :  : -1]
    if(string1 == string_rev):
        print("string is palindrome ")
    else:
        print("sting is not a palindrome ")


string3 = input("enter a string to check : ")
string3.upper()
plaindrome_check(string3)