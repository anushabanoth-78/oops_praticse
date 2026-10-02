class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposite(self,amount):
        self.balance +=amount
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficent balance")
        else:
            self.balance -=amount
    def show_balance(self):
        print(self.name, "→ Balance:", self.balance)

data1=BankAccount("Anusha",10000)

data2=BankAccount("Rahul",20000)

data3=BankAccount("priya",15000)
data1.deposite(5000)
data2.deposite(3000)
data3.withdraw(2000)
data1.withdraw(15000)

data1.show_balance()
data2.show_balance()

data3.show_balance()



