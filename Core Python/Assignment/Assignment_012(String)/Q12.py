#Q12. Python Program to count number of lowercase characters in a string.

str  = input("Enter a String:")

counter = 0

for val in str:
    if val.islower():
        counter = counter + 1
print(counter)
             