#Q3.Python Program to Detect if Two Strings are Anagrams.

a = input("Enter First String:")
b = input("Enter Second String:")

if sorted(a) == sorted(b):
    print("This is Anagram String")
else:
    print("This is not Anagram")
    
