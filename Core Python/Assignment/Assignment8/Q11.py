#Q11. WAP to check if givin number is Armstrong number or not.
# For each task creat separate functions.

def countdigits(num):
    return len(str(num))

def armstrongsum(num, count):
    temp = num
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum += digit ** count
        temp //= 10

    return sum

def checkarmstrong(num):
    count = countdigits(num)
    sum = armstrongsum(num, count)

    if sum == num:
        print(f"{num} is Armstrong Number")
    else:
        print(f"{num} is Not Armstrong Number")

num = int(input("Enter Number: "))
checkarmstrong(num)