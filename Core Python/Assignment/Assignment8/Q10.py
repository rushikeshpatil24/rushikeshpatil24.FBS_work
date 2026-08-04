# Q10. WAP to check if entered year is leap or not.

def leapyear(year):

    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(f"{year} is a Leap Year")
    else:
        print(f"{year} is Not a Leap Year")

year = int(input("Enter Year: "))
leapyear(year)