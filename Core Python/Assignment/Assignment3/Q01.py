## Write a program to check if the given number is positive or negative.

num = int(input('Enter a Number:'))

if(num == 0):
    print(f'{num} is Neutral')
    
elif(num > 0):
        print(f'{num} is Positive')
else:
    print(f'{num} is Negative:')