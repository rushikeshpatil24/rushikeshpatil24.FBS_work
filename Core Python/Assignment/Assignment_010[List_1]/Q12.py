# Q12.Write a program to create three lists of numbers, their squares and cubes.
li =[1,2,3,4,5,6,7,8]
li1 = []
li2 = []

for i in range(len(li)):
    square = li[i] ** 2
    li1.append(square)
    
    cube = li[i] ** 3
    li2.append(cube)

print("Numbers:",li)
print("Square of each number of list:",li1)
print("Cube of each number of list:",li2)