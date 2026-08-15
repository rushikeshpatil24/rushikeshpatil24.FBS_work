#Q8.Write a program to check whether a number is prime or not using recursion.

def prime(n, divisor):
    if divisor > n // divisor:
        return True

    if n % divisor == 0:
        return False

    return prime(n, divisor + 1)


n = int(input("Enter Number: "))

if n < 2:
    print("Not Prime")
elif prime(n, 2):
    print(f"{n} is Prime Number")
else:
    print(f"{n} is Not Prime")