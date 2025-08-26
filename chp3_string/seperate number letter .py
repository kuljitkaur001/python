# seperating the numbers and alphabets from list 
# when ever there is seperating concept ,,,, take the empty string with respect to asked question .......
# we have only o10 numbers . 1,2,3,4,5,6,7,8,9,0
#needs new varaible nu_m that helps to transfer numbers 

str = "string123"
all_num = ["1", "2","3", "4", "5", "6", "7", "8","9", "0"] 
number = []
letter = ""

for i in str:
    if i in all_num:
        nu_m = int(i)   #explicit typecasting ,
        print(type(nu_m)) #tell the type of variable                                                                                                                                  n
        number.append(nu_m)
    else:
        letter += i
print("number are  : ", number)
print("letter are  : ", letter)