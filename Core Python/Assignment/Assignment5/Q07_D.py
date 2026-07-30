# d. Saa2/2+a3/3+......+a10/10

a = int(input("Enter value of a: "))

sum = 0

for i in range(1, 11):
    sum += (a ** i) / i

print("Sum =", sum)