# for creating an exceptioner use class
class invalid_age(Exception):

    pass

age = int(input("enter your age :  "))
 
try:
    if(age <0):
        raise invalid_age("invalid  age, age can not be nagative ")

    else:
        print("age is valid ")

except invalid_age as e:
    print("error", e)

#raising exception