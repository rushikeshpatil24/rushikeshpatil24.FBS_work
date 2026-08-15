#Q6.Write a program to print the Fibonacci series using recursion.

def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Enter Number of Terms: "))

for i in range(n):
    print(fibonacci(i), end=" ")