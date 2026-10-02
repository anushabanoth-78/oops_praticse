class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
        
    def __str__(self):
        return f"Book: | {self.title} Author: {self.author}| price:{self.price}"
        
        
Book1 =Book("Python Basics","Anusha",500)
print(Book1)