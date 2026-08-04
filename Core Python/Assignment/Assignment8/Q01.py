#Q1.Write a program to calculate area of rectangle.

def areaofrect(l,w):
    
    area = l * w
    return area

l = float(input("Enter Length:"))
w = float(input("Enter Width:"))

result = areaofrect(l,w)
print("Area of Ractangle is:",result)