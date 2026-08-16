#Q7.Write a program to create a new list from an existing list which contains the cube of each number of the list.

li = [44,8,4,5,12,25,19]
li2 = []

for i in range(len(li)):
    cube =li[i] ** 3
    li2.append(cube)
print("Cube of each number of list:",li2)