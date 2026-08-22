# 10. Write a program to print list after removing even numbers.

li = [1,2,3,4,5,6,7,8,9,10]
new_li = []

for val in li:
    
    if val % 2 != 0:
        new_li.append(val)
        
print("List after removing Even Numbers:",new_li)