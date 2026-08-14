# Q2. Write a program to calculate simple interest based on Principal, Rate and Time
# (SI = P*R*T/100)

p = int(input("Enter Principle:"))
r = float(input("Enter Rate:"))
t = float(input("Enter Time:"))

si = (p * r * t) / 100

print("Simple intrest is :",si)