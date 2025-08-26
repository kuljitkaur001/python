'''Problem 4: Bank Account
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
    def __init__(self, account_holder, balance):
        self.accountant_holder = account_holder
        self.balance = balance
        # self.deposite = deposite
    
    def balance_(self, dep):
         self.balance += dep
         self.dep = dep
         print(f"current balance is = {self.balance}")
         print (f"after deposit  of {self.dep} , current balance is = {self.balance + self.dep}")

    def widthdrow(self,wid):
        
        self.wid = wid
        print(f"widthrowing amount is = {self.wid}")
        print(f'after widthrowing {self.wid},  the current amount is ={self.balance-self.wid}')
        return self.balance-self.wid

object1 = bank_account("kuljit kaur ", 0 )
dep = int(input("enter the deposited amount : "))
object1.balance_(dep)

wid = int(input("enter how much money do you want to widthrow : "))
object1.widthdrow(wid)
        