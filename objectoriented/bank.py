#account creation:your SBI account has been created with amount 2500
# your current balance 7500
# account deposited with 2500
# available balance 5000
class Bank:
    bankname="SBI"                               #class variable(static variavble)
    def accountcreation(self,accountno,name):
        self.accountno=accountno
        self.name=name
        self.minimumbal=5000
        self.balance=self.minimumbal
    def deposit(self,amount):
        self.amount=amount
        self.balance+=self.amount
        print("your",Bank.bankname,"account has been created with amount",self.amount)
        print("your current balance=",self.balance)
    def withdraw(self,amount):
        self.amount=amount
        if self.amount > self.balance:
            print("insufficient balance")
        else:
            print("account debited with",self.amount)
            self.balance-= self.amount
            print("available balance",self.balance)
obj=Bank()
obj.accountcreation(123,'abc')
obj.deposit(2500)
obj.withdraw(1500)