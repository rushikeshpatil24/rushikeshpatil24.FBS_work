# Q3. Create a class Shirt with members as sid, sname, type, price and size.
# Add Constructor (parameterized and parameterless), Destructor and ShowBook.

class Shirt:
    def __init__(self, sid=0, sname="", type="", price=0, size=""):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    def ShowBook(self):
        print("Shirt ID:", self.sid)
        print("Shirt Name:", self.sname)
        print("Type:", self.type)
        print("Price:", self.price)
        print("Size:", self.size)

    def __del__(self):
        print("Shirt object destroyed")


print("Parameterized Constructor:")
s1 = Shirt(101, "Formal Shirt", "Formal", 1200, "Large")
s1.ShowBook()

print("\nParameterless Constructor:")
s2 = Shirt()
s2.ShowBook()
