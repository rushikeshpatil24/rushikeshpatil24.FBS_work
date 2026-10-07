# Find words having less than 5 letters

s = input("Enter a string: ")

result = [i for i in s.split() if len(i) < 5]

print(result)
