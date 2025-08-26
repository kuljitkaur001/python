try:
    a = int("hello"  )
    b = 5     
    c = a/b  
    print(c)
except ValueError:
    print("Invalid value!")
except ZeroDivisionError:
    print("Cannot divide by zero!")


try:
    a = 12
    b = 0   
    c = a/b  
    print(c)
except ValueError:
    print("Invalid value!")
except ZeroDivisionError:
    print("Cannot divide by zero!")



try:
    a = 12
    b = 5  
    c = a/b  
    print(c)
except ValueError:
    print("Invalid value!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

finally: #keywword...... continue evne if have error 
    print("execution finish ")



try:
    a = 12
    b = 5  
    c = a/b  
    # print(c)
except ValueError:
    print("Invalid value!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

else:
    print(c)

finally: #keywword...... continue evne if have error 
    print("execution finish ")