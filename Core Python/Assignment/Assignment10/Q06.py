# Q6.Write a program to remove duplicates from the list.

li = [12,64,83,93,83,64,32,12]
new_li = []

for val in li:
    if val not in new_li:
        new_li.append(val)
        
print("List after removing duplicate values:",new_li)    