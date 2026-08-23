# Q4. Python Program to Form a New String where the First Character and
# # the Last Character have been Exchanged.

str = input("Enter a String:")

first = str[0]
last = str[-1]
middle = str[1:-1]

new_str = last + middle + first

print("New String:",new_str)
