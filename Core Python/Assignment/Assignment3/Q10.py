## Write a program to check if persion is eligible to marry or not(male age>=21) and (female>=18).

gender = input('Enter male/female:')
age = int(input('Enter Age:'))

if(gender == 'male'):
    if(age >= 21):
        print('Boys is eligible for Marrige')
    else:
        print('Boy is not Eligible for Marrige')
        
else:
    if(age >=18):
        print('Girl is eligible for Marrige')
    else:
        print('Girl is not Eligible for Marrige')