#Q10.Python Program to Take in Two Strings and Display the Larger String
## without Using Built-in Functions.

str1 = input("Enter First String:")
str2 = input("Enter Second String:")

count_1 = 0
count_2 = 0

for val in str1:
    count_1 = count_1 + 1
    
for val  in str2:
    count_2 = count_2 + 1
    
if count_1 == count_2:
    print("Both Strings ar equel")
elif count_1 > count_2:
    print("Larger String:",str1)
else:
    print("Larger String:",str2)