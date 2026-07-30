# Q7.Write program to solve the following series:

# a. 1!2!3!4!+.....n!


num = int(input("Enter Number:"))

sum = 0

for i in range(1, num + 1):
    fact = 1

    for j in range(1, i + 1):
        fact *= j

    sum += fact

print("Sum =", sum)