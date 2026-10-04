# Q2. Create a class Product with members as pid, pname, price and quantity.
# Add Constructor (parameterized and parameterless), Destructor and ShowBook.

class Product:
    def __init__(self, pid=0, pname="", price=0, quantity=0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def ShowBook(self):
        print("Product ID:", self.pid)
        print("Product Name:", self.pname)
        print("Price:", self.price)
        print("Quantity:", self.quantity)

    def __del__(self):
        print("Product object destroyed")


print("Parameterized Constructor:")
p1 = Product(101, "Laptop", 50000, 2)
p1.ShowBook()

print("\nParameterless Constructor:")
p2 = Product()
p2.ShowBook()
