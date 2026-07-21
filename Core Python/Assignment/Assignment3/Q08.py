## Write a program to prompt user to enterd userid and password.
# After verifying userid and password to display a 4 digit random number  and ask user to enter the same.
# If user  enters the same number  then show him success message otherwise failed.(Somthing like Captcha).


import random

userid = input('Enter Userid:')
password = input('Enter Password:')

if(userid == 'admin@678' and password == 'rishi99'):
    captch = random.randint(1000,9999)
    print(f'Your Captcha = {captch}')
    chuser = int(input('Enter your Captcha=>'))
    if chuser == captch:
        print('User login successfully')
    else:
        print('Invalid captcha')
else:
    print('User is Invalid')
