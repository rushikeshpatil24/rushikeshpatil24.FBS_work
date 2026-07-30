# e. xx2/3 + x3/5 - x4/7 + .... to n terms

x = int(input("Enter x: "))
num = int(input("Enter number of terms: "))

sum = 0
sign = 1
den = 1

for i in range(1, num + 1):

    term = sign * (x ** i) / den
    sum += term

    sign *= -1
    den += 2

print("Sum =", sum)