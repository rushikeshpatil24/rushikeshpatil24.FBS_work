## Write a program to input all sides of a triangle and check whether triangle is valid or not.

side1 = float(input('Enter side1:'))
side2 = float(input('Enter side2:'))
side3 = float(input('Enter side3:'))

# sum = side1 + side2 > side3

if(side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    print('Triangle is valid:')
else:
    print('Triangle  is Invalid:')