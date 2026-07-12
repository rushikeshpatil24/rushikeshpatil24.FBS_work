### Write a program to find Quotient and remainder of two number

#take input for dividend and divisor

Dividend = int(input('Enter Dividend:'))
Divisor = int(input('Enter Divisor:'))

#Perform Operation

Q = Dividend // Divisor
R = Divisor % Divisor

print(f'Quotient is {Q} and Remainder is {R}')