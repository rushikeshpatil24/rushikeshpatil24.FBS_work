# Television

class Television:
    def __init__(self):
        self.model = 0
        self.screen_size = 0
        self.price = 0

    def getdata(self):
        self.model = input("Enter model number: ")
        self.screen_size = float(input("Enter screen size: "))
        self.price = float(input("Enter price: "))

        if len(self.model) != 4:
            raise ValueError("Model number must contain 4 digits")

        if self.screen_size < 12 or self.screen_size > 70:
            raise ValueError("Screen size must be between 12 and 70 inches")

        if self.price < 0 or self.price > 5000:
            raise ValueError("Price must be between 0 and 5000")


    def showdata(self):
        print("Model Number:", self.model)
        print("Screen Size:", self.screen_size)
        print("Price:", self.price)


t = Television()

try:
    t.getdata()
    t.showdata()
except ValueError as e:
    print("Error:", e)
    t.model = 0
    t.screen_size = 0
    t.price = 0
    t.showdata()
