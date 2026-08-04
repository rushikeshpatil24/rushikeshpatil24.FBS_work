#Q4. Sum of all odd numbers between 1 to n.

def oddNo(num):
    
    total = 0
    
    for i in range(1,num+1):
        if(i % 2 != 0):
            total += i
            
            
    return total
    
num = int(input("Enter Number:"))

result = oddNo(num)
print("Sum of series is:",result)
        
        