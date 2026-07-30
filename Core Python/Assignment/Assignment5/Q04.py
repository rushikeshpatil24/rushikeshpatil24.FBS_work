#05. Write a program to print Armstrong number with in a given range.

first = int(input("Enter First Number :"))
end = int(input("Enter Second Number :"))

for num in range (first,end+1):

    temp = num
    count = len(str(num))
    sum = 0

    while (num > 0):
        d = num % 10
        sum = sum + (d**count)
        num = num // 10

    if temp == sum :
        print(F"{sum} is Armstrong Number ")