## Write a program to check if given 3 digit number is Palindrome or not :

num = int(input("Enter Three Digit Number :"))

temp = num

d1 = num % 10
num = num // 10 

d2 = num % 10
num = num // 10 

d3 = num % 10
num = num // 10 

Rev = d1*100+d2*10+d3

print("Reverse of Three Digit No :",Rev)

if ( temp == Rev ):
    print("Number is Palindrome")
else:
    print("Number is Not Palindrome ")
