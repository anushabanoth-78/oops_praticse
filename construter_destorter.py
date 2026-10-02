class Laptop:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
        print("Laptop created")
    def __del__(self):
        
       print("Laptop object destroyed")
data1=Laptop("Dell",50000)
print(data1.brand,data1.price)
del data1