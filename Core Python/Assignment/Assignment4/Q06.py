#6. Write a program to print to check if a given number is prime or not.

n = int(input('Enter a  number:'))

if(n > 1):
    
    for i in range(2,n):
        
        if(n % i == 0):
            print(f'{n} is not Prime Number')
            break
    else:
        print(f'{n} is a Prime Number')
            
else:
    print(f'{n}  is not a Prime Number:')
            