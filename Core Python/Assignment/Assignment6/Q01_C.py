# Q1. Write a program print following patterns :

for i in range(4):

    k = 1

    for j in range (4-i-1):
        print(" ",end=" ")

    for j in range(i+1):
        print(k ,end="   ")
        k = k * (i-j) // (j+1)

    print()