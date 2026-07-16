### Write a program to convert a days into years,weaks and days.

days  = int(input('Enter Days:'))

years = days // 365
remaining = days % 365
weeks = remaining // 7
days = remaining % 7

print(f'Year:{years},Weeks:{weeks},Days:{days}')

