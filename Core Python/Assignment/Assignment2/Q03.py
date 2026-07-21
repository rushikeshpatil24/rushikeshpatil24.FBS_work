## Convert distance given in feet and inches into meter and centimeter.

feet = float(input('Enter feet:'))
inches = float(input('Enter Inches:'))

total_inches = (feet * 12) + inches

meters = total_inches * 0.0254
centimeters = total_inches *2.54

print('Total_inches is:',total_inches)
print('Meters:',meters)
print('Centimeters:',centimeters)