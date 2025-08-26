class bank_account:
    def __init__(self, account_holder, balance):
        self.accountant_holder = account_holder
        self.balance = balance

    def balance_(self, dep):
        print(f"current balance is = {self.balance}")
        print(f"after deposit of {dep}, current balance is = {self.balance + dep}")

    def widthdrow(self, wid):
        print(f"widthrowing amount is = {wid}")
        print(f"after widthrowing {wid}, the current amount is = {self.balance - wid}")


object1 = bank_account("kuljit kaur", 0)

dep = int(input("enter the deposited amount : "))
object1.balance_(dep)

wid = int(input("enter how much money do you want to widthrow : "))
object1.widthdrow(wid)
