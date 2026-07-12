### Write a program to  enter p,t,r and  calculate simple intrest

#Take input for p,t,r from user

P = int(input('Enter Principle amount:'))
T = int(input('Enter Time:'))
R = float(input('Enter Rate:'))

# perform operation

si = (P * R * T) / 100

#Display Output

print("Simple Intrest is:",si)