class account:
    def __init__(self, acount_holder, balance): #firts function , we can pass directly values in the object while creating the object o f class 
        self.acountholder= acount_holder #accessing the acount holder 
        self.balance = balance #accessing the balance 

    def deposite(self, dep_ammount): #this self taking the previous method values , and a new parametr , dep_amt
        self.depositeamt = dep_ammount #accessing the ne paramter 
        self.balance += dep_ammount # updating the balance , while accessing the values from an already creted funvtion use "self" keyword 
 
    def show(self): #showing values 
        print(f"{self.acountholder} just got credited an ammount {self.depositeamt} and now the balance is {self.balance}")


objectt = account("kuljit", 0) #cretaing an object, and passing values ot first method to i,e init 
objectt.deposite(2000) # pasing values to deposit function while calling 
objectt.show() # simply calling show function 