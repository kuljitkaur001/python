# You have a variable budget and a variable price. Write a conditional statement to check if budget is greater than or equal to price. If true, print "Purchase possible", otherwise print "Not enough budget".

budget =int(input("\n enter you budget : ")) 
price = int(input("\n enter price  for item you want buy : "))
if(budget==price):
    print("\n purchase possible")
else:
    print("\n not anough budget")
