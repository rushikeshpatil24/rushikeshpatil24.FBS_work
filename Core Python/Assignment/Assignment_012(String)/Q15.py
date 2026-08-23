#Q15.Python Program to find larger string without using built-in functions.

str1 = input("Enter First String:")
str2 = input("Enter Second String:")

count_1 = 0
count_2 = 0

for i in str1:
    count_1 = count_1 + 1
    
for i  in str2:
    count_2 = count_2 + 1
    
if count_1 == count_2:
    print("Both Strings ar equel")
elif count_1 > count_2:
    print("This is Larger String:",str1)
else:
    print("This is Larger String:",str2)