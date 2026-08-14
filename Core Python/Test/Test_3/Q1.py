#Q 1. Write a program to find the area and perimeter of following figure (Accept the
# length, breadth and radius from user:

l = float(input("Enter length: "))
r = float(input("Enter radius: "))

b = 2 * r

area = (l * b) + (3.14 * r * r / 2)
peri = (2 * l) + (2 * r) + (3.14 * r)

print("Area =", area)
print("Perimeter =", peri)