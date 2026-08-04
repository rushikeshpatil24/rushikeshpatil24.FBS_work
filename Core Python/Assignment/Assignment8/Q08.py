#Q8. Write a program to find reverse of a number.

def reverseNo(num):
    temp = num 
    rev = 0
    
    while(temp > 0):
        digit = temp % 10
        rev = rev * 10 + digit
        temp //= 10
    return rev

num = int(input("Enter Number:"))
result = reverseNo(num)
print("Reverse Number is :",result)