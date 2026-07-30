#5. Write a program to print fibonacci  series  upto n.


n = int(input('Enter a Number of Terms:'))

a = -1 
b = 1

for i  in range(n):
    c = a + b
    print(c)
    
    a = b 
    b = c