## Input 5 subject marks  from user and display grade(eg.first class,second class..).

s1=int(input('Enter sub1:'))
s2=int(input('Enter sub2:'))
s3=int(input('Enter sub3:'))
s4=int(input('Enter sub4:'))
s5=int(input('Enter sub5:'))

obtained_marks = s1 + s2 + s3 + s4 +s5
per = (obtained_marks / 500) * 100
print(f'Percentage is:{per}')

if(per >= 90):
    print('first Class')
elif(per >= 75):
    print('Second Class')
elif(per >=45):
    print("Third Class")
elif(per >= 35):
    print(' student is Pass')
else:
    print('student is fail')