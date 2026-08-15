# Q10.Write a program to remove all occurrences of a given element in the list.

num = int(input("Enter Element:"))
li = [10,20,30,40,50,60]
li2 = []
for val in li:
    if val != num:
        li2.append(val)
print(li2)
