### Write A program to enter  p,t,r and calculate Compound Intrest.

P = float(input('Enter Principle Amount:'))
R = float(input('Enter Rate:'))
T = float(input('Enter Time:'))

Amount = P * ((1 + (R / 100))) ** T
CI = Amount - P

print('compound Intrest:',CI)
