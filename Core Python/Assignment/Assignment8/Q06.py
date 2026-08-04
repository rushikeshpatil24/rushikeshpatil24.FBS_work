#Q6.Write a program to find print the following Fibonacci series using functions:

def fibo(num):
    a = -1
    b = 1
    
    for i in range(1,num+1):
        c = a+b
        print(c) 
           
        a = b
        b = c
    
num = int(input("Enter Number:"))
print("Fibonacci Series is:")
fibo(num)