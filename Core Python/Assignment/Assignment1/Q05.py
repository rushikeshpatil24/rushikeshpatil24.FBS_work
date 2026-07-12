### Write A program to enter  p,t,r and calculate Compound Intrest.

# take input for p,t,r

P = float(input('Enter Principle Amount:'))
R = float(input('Enter Rate:'))
T = float(input('Enter Time:'))

# perform Operation

Amount = P * ((1 + (R / 100))) ** T
CI = Amount - P

# Diplay Output

print('compound Intrest:',CI)