def palindorm(S):
    n = len(S)
    is_palindrome = True 
    for i in range(n):
        if S[i]==S[n-1]:
            n-=1   
        else:
            is_palindrome = False
    
    if is_palindrome:
        print("palindrome ") 
    else:
        print("not a palindrome ")


palindorm("madam")

