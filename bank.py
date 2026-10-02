class Bank:
    # Class-level data
    interest_rate = 5

    # Constructor
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    # Class method
    @classmethod
    def change_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate

    # Static method
    @staticmethod
    def withdrawal(amount):
        if amount > 0:
            print("Valid withdrawal")
        else:
            print("Invalid withdrawal")


# Creating objects
data1 = Bank("Anusha", 5000)
data2 = Bank("Bhanusri", 40000)

# Changing class-level interest rate
Bank.change_interest_rate(7)

# Display interest rate
print("Interest Rate:", Bank.interest_rate)

# Testing static method
Bank.withdrawal(5000)
Bank.withdrawal(-100)