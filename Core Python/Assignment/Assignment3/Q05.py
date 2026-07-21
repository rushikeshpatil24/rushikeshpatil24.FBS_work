## Write a program to check whether the triangle is equilateral,isosceles or scalene triangle.

a = int(input('Enter side1:'))
b = int(input('Enter side2:'))
c = int(input('Enter side3:'))

if(a == b == c):
    print('Triangle is equilateral')
elif(a == b or b == c or a == c):
    print('Triangle is Isosceles')
else:
    print(('Triangle is scalene'))