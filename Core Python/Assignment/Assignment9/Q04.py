#Q4.Write a program to find the sum of n numbers using recursion.

def add(n):
    if n > 0:
        return n + add(n - 1)
    else:
        return  0

n = int(input("Enter Number:"))
res = add(n)
print("Sum of Series is:",res)