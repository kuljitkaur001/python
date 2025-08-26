# Given a variable day which can be any day of the week, write a conditional statement to print "Weekend" if the day is "Saturday" or "Sunday", otherwise print "Weekday".

day = input("enter day : ")
# day1 = "Monaday"
# day2 = "Tuesday"
# day3 = "Wednesday"
# day4 = "Thurday"
# day5 = "Friday"
# day6 = "Saturday"
# day7 = "Sunday"

if(day == "Saturday" or day == "Sunday"):
    print("this is a weekend ")
else:
    print("working day ")