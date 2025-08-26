'''
Problem 4: Bank Account
Create a class named BankAccount with the following attributes:

account_holder (string)
balance (float, default value 0)
Write methods:

deposit to add an amount to the balance.
withdraw to subtract an amount from the balance, ensuring it doesn't go negative.
display_balance to print the current balance.
Create an object, deposit and withdraw money, and display the balance.
'''

class bank_account:
    # balance = 0 
    def __init__(self, account_holder, balance ):
        self.accountholder = account_holder
        self.balance = balance

    def deposite(self, dep_ammount):
        self.deposit = dep_ammount
        self.balance+= dep_ammount
    
    # def withdrow(self, wid_amount):
    #     self.wid_amount = wid_amount
    #     if wid_amount<=self.balance:
    #         self.balance+=wid_amount

    # def balance(self):
    #     return (self.wid
    def display(self):
        print(self.balance)


object1= bank_account("pinki", 0 )
# print(object1.accountholder)
# print(object1.balance)

deposition = int(input("enter deposit ammount : "))
# print(deposition)
object1.deposite(deposition)
object1.display()

