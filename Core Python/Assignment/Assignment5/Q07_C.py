#c.Find the sum of a geometric series from 1 to n where the common ratio is 2.

num = int(input("Enter number of terms: "))

sum = 0

for i in range(num):
    sum += 2 ** i

print("Sum =", sum)