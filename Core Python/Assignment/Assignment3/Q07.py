## Write a program to check if user has enterd correct userid or password.

userid = input('Enter Userid:')
password = input('enter password:')

if(userid == 'admin@123' and password == 'rishi009'):
    print('Loggin Successful')
else:
    print('Invalid userid and password')