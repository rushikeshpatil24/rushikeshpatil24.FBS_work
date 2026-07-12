### Write A program to enter  p,t,r and calculate Compound Intrest.

#take input for a,b,c from user.

a = float(input('Enter  Value of a:'))
b = float(input('Enter value of b:')) 
c = float(input('Enter Value of c:'))
 
# perform Operation.
D = b ** 2 - 4 * a * c
 
Root1 = (-b +  D ** 0.5) / (2 * a)
Root2 = (-b -  D ** 0.5) / (2 * a)

# Display Output.

print("Root1 is:",Root1)
print("Root2 is:",Root2)