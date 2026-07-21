## Write a program to check if given 3 digit number is Palindrome or not.

num = int(input('Entre 3 digit Number:'))

temp = num
first = num // 100
last = num % 10

if(first == last):
    print(f'{num} is Palindrome')
else:
    print(f'{num} is not Palindrome')
