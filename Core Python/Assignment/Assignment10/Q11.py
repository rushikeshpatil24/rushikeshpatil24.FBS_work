# Q11.Write a program to print all numbers which are divisible by m and n in the list.

li = [10, 20, 30, 40, 60, 90, 120, 150]

m = int(input("Enter m:"))
n = int(input("Enter n:"))

for val in li:
    if val % m == 0 and val % n == 0:
        print(val)

