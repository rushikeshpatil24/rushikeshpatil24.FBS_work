# Q2. Python Program to Remove the nth Index Character from a Non-Empty
# # String

s = input("Enter a string: ")
n = int(input("Enter the index to remove: "))

result = s[:n] + s[n+1:]

print("String after removing character:", result)