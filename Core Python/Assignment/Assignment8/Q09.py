#Q9. Write a program to check if entered number is a Palindrome or not.

def palindrome(num):
     
    temp = num
    rev = 0 
     
    while temp > 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp //= 10

    if (rev == num):
        print(f"{num} is Palindrome Number")
    else:
        print(f"{num} is Not Palindrome Number")
        
num = int(input("Enter Number:"))
palindrome(num)