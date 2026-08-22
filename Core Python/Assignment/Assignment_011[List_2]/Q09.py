# 9. Write a program to create three lists of numbers, their squares and cubes.

numbers = []
squares = []
cube = []

for i in range(1,6):
    numbers.append(i)
    squares.append(i ** 2)
    cube.append(i ** 3)

print("Numbers is:",numbers)
print("Squares is:",squares)
print("Cubes   is:",cube)
