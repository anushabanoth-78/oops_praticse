class Bankaccount:
    def __init__(self,account_holder,account_number,balance):
        self.account_holder=account_holder
        self.account_number=account_number
        self.balance=balance
s1=Bankaccount("Anusha",123,5000)
print(s1.account_holder)
print(s1.account_number)
print(s1.balance)

