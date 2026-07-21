## Write a program to reverse three digit of number.

num = int(input('Enter a Number:'))

first  = num // 100
middle = (num // 10) % 10
last   = num % 10

reverse = (last * 100) + (middle * 10) + first
print('Reversed Number:',reverse)