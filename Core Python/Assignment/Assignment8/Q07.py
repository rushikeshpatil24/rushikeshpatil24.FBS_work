# Q7. Write a program to find sum of digits of a number.

def sumofdigits(num):
    total = 0

    while num > 0:
        digit = num % 10
        total += digit
        num //= 10

    return total

num = int(input("Enter Number: "))
result = sumofdigits(num)
print("Sum of Digits is:", result)