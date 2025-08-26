# You have a variable year. Write a conditional statement to check if year is a leap year. If true, print "Leap year", otherwise print "Not a leap year".

year = int(input("\n enter any year to check : "))
if(year%4==0):
    print("it is leap year")
else:
    print("it is not an leap year")