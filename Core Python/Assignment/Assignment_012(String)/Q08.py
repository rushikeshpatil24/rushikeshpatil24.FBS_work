#QS8. Python Program to Remove the Characters of Odd Index Values in a
# # String.

str  = input("Enter String:")

result = ""

for val in range(0,len(str)):
    if val  % 2 == 0:
        result = result + str[val]
        
print(result)