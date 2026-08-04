#Q3.Write a program to find sum of following series using functions:

# a. 1+2+3+4+......+n

def sumofseries(num):
    
    sum = 0
    for i in range(1,num+1):
        sum+= i
    return sum
    
num = int(input("Enter Number:"))

result = sumofseries(num)
print("Sum of Series is:",result)