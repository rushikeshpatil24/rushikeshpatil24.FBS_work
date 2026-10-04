# Q2. Create a class Product with members as pid, pname, price and quantity.
# Constructor, Destructor, ShowBook, static member discount
# and method for applying discount on product price.

class Product:
    discount = 10

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

    def apply_discount(self):
        discounted_price = self.price - (self.price * Product.discount / 100)
        return discounted_price

    def __del__(self):
        print("Product object destroyed")


p1 = Product(101, "Laptop", 50000, 2)
p1.ShowBook()
print("Discount:", Product.discount, "%")
print("Price after discount:", p1.apply_discount())
