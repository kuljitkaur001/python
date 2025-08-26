# Given a variable time representing the hour of the day in 24-hour format, write a conditional statement to print "Good morning" if time is between 6 and 12, "Good afternoon" if time is between 12 and 18, and "Good evening" if time is between 18 and 24.

time = int(input("\n enter you cureent time : "))
if(6<time<12 ):
    print("good morning")
elif(12<time<18):
    print("good afternoon")
elif(18<time<24):
    print("good evening ")
else:
    print("have a good day ")
