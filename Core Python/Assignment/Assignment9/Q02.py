#Q2.Write a program to check if a given number is an Armstrong number or not using a recursive function.

def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)


def armstrong(n, digits, original):
    if n == 0:
        return 0

    d = n % 10
    return d ** digits + armstrong(n // 10, digits, original)


n = int(input("Enter Number: "))

digits = count_digits(n)
res = armstrong(n, digits, n)

if res == n:
    print(f"{n} is Armstrong Number")
else:
    print(f"{n} is Not Armstrong Number")