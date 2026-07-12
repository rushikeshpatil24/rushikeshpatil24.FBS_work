### Write a program to convert a days into years,weaks and days.

# Take input for day 

days  = int(input('Enter Days:'))

#perform Operation
 
years = days // 365
remaining = days % 365
weeks = remaining // 7
days = remaining % 7

# Display output

print(f'Year:{years},Weeks:{weeks},Days:{days}')

