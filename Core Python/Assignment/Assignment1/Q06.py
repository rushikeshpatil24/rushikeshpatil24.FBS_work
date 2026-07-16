### write a program to  input for  two angle from used and find third angle of the triangle.

angle1 = float(input('Enter Angle1:'))
angle2 = float(input('Enter Angle2:'))

third_angle = 180 - (angle1 + angle2)

print('Third Angle of the triangle is:',third_angle)
