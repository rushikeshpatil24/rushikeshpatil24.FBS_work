# Q10. Write a program to check if given number is Perfect Number.

num = int(input("Enter Number: "))

sum = 0

for i in range(1, num):
    if num % i == 0:
        sum = sum + i

if sum == num:
    print("Perfect Number")
else:
    print("Not Perfect Number")