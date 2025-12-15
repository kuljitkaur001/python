def changingpositions(s):
    first = s[0]
    last = s[-1]
    midlle = s[1:-1]
    
    sum = last+midlle+first
    print(sum)

user = input("enter a string  to change first and last positions  ")
changingpositions(user)

