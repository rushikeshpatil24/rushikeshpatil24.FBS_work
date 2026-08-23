#Q13.Python Program to count number of digits and letters in a string.

str = input("Enter a String:")
 
letters = 0
digits = 0

for val in str:
    if val.isalpha():
        letters += 1
        
    elif val.isdigit():
        digits += 1
       

print("Number of letters:",letters)
print("Number of digits:",digits)