# withdrowing 

class account:
    def __init__(self, account_holder, balance):
        self.acountholder = account_holder
        self.balance = balance

    def dep(self, dep_amt):
        self.depamount = dep_amt
        self.balance += dep_amt
    
    def withdrow(self, wid_amt):
        self.withrow_amt = wid_amt
        if (wid_amt >self.balance):
            print("insufficet balance ")
        elif wid_amt < 0:
            print("withdrow can not be possible ")
        else:
            self.balance= wid_amt
    def display(self):
        print(f"balance amount {self.balance}")

object11 = account("kuljit", 0 )
object11.dep(5000)
object11.withdrow(2000)
object11.display()