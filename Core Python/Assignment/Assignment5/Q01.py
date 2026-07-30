# Q1. Write a program to prompt user to enter userid and password.
# If Id and password is incorrect give him chance to re-enter the credentials.
# Let him try 3 times. After that program to terminate.

uid = 'userid'
pwd = 'password'
    
for i in range(3):
    userid = input("Enter User ID: ")
    password = input("Enter Password: ")

    if userid == 'admin@123' and password == 'rishi24':
        print("Login Successful")
        break
    else:
        print("Incorrect Credentials")

else:
    print("Account Locked")