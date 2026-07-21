 ## Write a program to input angles of triangle and check whether triangle is valid or not.
 
angle1 = float(input('Enter Angle1:'))
angle2 = float(input('Enter Angle2:')) 
angle3 = float(input('Enter Angle3:'))

sum = angle1 + angle2 + angle3

if(sum == 180 and angle1 > 0  and angle2 > 0 and angle3 > 0):
    print('Triangle is valid')
else:
    print('Triangle is Invalid:')