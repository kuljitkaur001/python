# palidrome ..... 
# rwterive lenght of string 
#  2 var needed , if for first index (by default in for loop ), one for last index(var which have store length )
# tzke another variable , as "is_palidorome = True , or false " ...

# we need exactly 2 times if stmt, one in for loop , and anoter just outside the for loop 
# zlso need bool value , if you assign true first , make it false in else ,



string = input("enter a string : ")
n = len(string) #shows how mnuch enteries we have in the list , not how much indexes we have .. 
is_palindrome = True

for i in range(0,n): # i start moving from 0 and go uptp n-1 index val . , n is length , that s we already reterived
    if(string[i]== string[n-1]): #start comparing indexes, not first and last but all , here in if , what we write , exactly what we reteivie 
        n-=1  #decrementing the last variable , becoz the first variable which is on the first index will automatically incresing, if the condition gets true , the 
    else:
        is_palindrome = False  
if is_palindrome:  
    print("palindrome")
else:
    print("not a palindrome")

    