#Q3.Write a program to find sum of following series using functions:

# b. 1!+2!+3!+4!+......+n!

def sumofseries(num):
    fact = 1
    total = 0
    
    for i in range(1,num+1):
        fact *= i
        total += fact
    return total

num = int(input("Enter Number:"))

result = sumofseries(num)
print("Sum of Series is:",result)


        