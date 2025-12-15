# for any unknown error 
try: 
    a = 10
    b= 0
    c= a/b
    # print(c)

except Exception as e : 
    print(e)
    print("invalid input, please provide right input ")
else:
    print(c)