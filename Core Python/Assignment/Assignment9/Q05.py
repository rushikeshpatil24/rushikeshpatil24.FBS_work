#Q5.Write a program to find the factorial of a number using recursion.

def factorial(n):
    if n == 0 or n ==1:
        return  1
    return n * factorial (n -  1)
    
    
n = int(input("Enter Number:"))
res = factorial(n)
print("Factorial is:",res)
