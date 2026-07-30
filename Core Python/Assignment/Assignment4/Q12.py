# Q12. Write a program to check if given number is Armstrong number or not. (Hint: 1531*1*1+5*5*5+3*3*3, 16341*1*1*1+6*6*6*6+3*3*3*3+4*4*4*4).

n = int(input("Enter number: "))

temp = n
count = len(str(n))
sum = 0

while temp > 0:
    digit = temp % 10
    sum = sum + digit ** count
    temp = temp // 10

if sum == n:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
