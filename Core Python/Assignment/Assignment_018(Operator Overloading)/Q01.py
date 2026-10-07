# Complex Number

class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, c):
        return Complex(self.real + c.real, self.imag + c.imag)

    def __str__(self):
        return str(self.real) + " + " + str(self.imag) + "i"

    def __del__(self):
        pass


c1 = Complex(2, 3)
c2 = Complex(4, 5)

c3 = c1 + c2

print("First complex number:", c1)
print("Second complex number:", c2)
print("Addition:", c3)
