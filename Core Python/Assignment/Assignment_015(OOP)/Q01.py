# Q1. Create a class Book with members as bid, bname, price and author.
# Add Constructor (parameterized and parameterless), Destructor and ShowBook.

class Book:
    def __init__(self, bid=0, bname="", price=0, author=""):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author

    def ShowBook(self):
        print("Book ID:", self.bid)
        print("Book Name:", self.bname)
        print("Price:", self.price)
        print("Author:", self.author)

    def __del__(self):
        print("Book object destroyed")


print("Parameterized Constructor:")
b1 = Book(101, "Python Programming", 500, "Rishikesh")
b1.ShowBook()

print("\nParameterless Constructor:")
b2 = Book()
b2.ShowBook()
