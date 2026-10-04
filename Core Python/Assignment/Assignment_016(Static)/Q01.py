# Q1. Create a class Book with members as bid, bname, price and author.
# Constructor, Destructor, ShowBook and static variable count
# to maintain count of objects created.

class Book:
    count = 0

    def __init__(self, bid=0, bname="", price=0, author=""):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        Book.count += 1

    def ShowBook(self):
        print("Book ID:", self.bid)
        print("Book Name:", self.bname)
        print("Price:", self.price)
        print("Author:", self.author)

    def __del__(self):
        print("Book object destroyed")


b1 = Book(101, "Python Programming", 500, "Rishikesh")
b2 = Book(102, "Java Programming", 600, "ABC")
b3 = Book()

b1.ShowBook()
b2.ShowBook()

print("Total objects created:", Book.count)
