# Q7. Write a program to find sum of digits using recursion.

def sum_digits(n):
    if n == 0:
        return 0

    d = n % 10

    return d + sum_digits(n // 10)


n = int(input("Enter Number: "))

res = sum_digits(n)

print("Sum of digits is:", res)