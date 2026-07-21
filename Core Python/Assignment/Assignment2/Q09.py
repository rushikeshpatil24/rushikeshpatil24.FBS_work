 #Write a program to swap two number without using third variable.

x = int(input('Enter Value of X:'))
y = int(input('Enter value of Y:')) 
print(f"Before swapping x = {x} & y = {y}")

x,y = y,x
print(f"After swapping x = {x} & y = {y}")
