# Q1.Write a program to find the sum of the series 1! + 2! + 3! + 4! + ... + n! using recursive functions.
# (Use two recursive functions: one for factorial and one for sum.)

def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)


def sum_fact(n):
    if n == 0:
        return 0
    return fact(n) + sum_fact(n - 1)


n = int(input("Enter Number: "))
res = sum_fact(n)

print("Sum of factorials is:", res)