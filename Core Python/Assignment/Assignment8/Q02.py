#Q2.Write a program to calculate area of Circle.

def areaofcircle(r):
    
    area = 3.14 * (r ** 2)
    return area

r = float(input("Enter Radius:"))

result = areaofcircle(r)
print("Area of Circle is:",result)