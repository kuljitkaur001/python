# whether a student has passed or failed if it requires a total of 40% and atleast 33% in each sub to pass , assume  subjects  and take  marks as an input from user 
a = int(input("enter marks of subject 1 : "))
b = int(input("enter marks of subject 2 : "))
c = int(input("enter marks of subject 3 : "))
total_percentage = ((a+b+c)/300*100)
print(total_percentage)

if(total_percentage>= 33):
    print("result : pass ")

else:
    print("result : fail")
