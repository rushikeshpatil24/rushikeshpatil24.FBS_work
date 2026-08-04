#Q3.Write a program to find sum of following series using functions:

# c. 1^1 + 2^2 + 3^3 +......n^n

def sumofseries(num):
    total = 0
    
    for i in range(1,num+1):
        total += i ** i
        
    return total

num = int(input("Enter Number:"))

result = sumofseries(num)
print("Sum of Series is:",result)

