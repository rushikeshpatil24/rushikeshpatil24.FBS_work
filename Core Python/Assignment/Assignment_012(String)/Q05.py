#Q5. Python Program to Count the Number of Vowels in a String.

str = input("Enter a String: ")

count = 0

for val in str:
    if val.lower() in "aeiou":
        count += 1

print("Number of vowels:", count)