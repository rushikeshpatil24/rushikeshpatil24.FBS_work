#  Q1. Write a program print following patterns :

#  g  :


for i in range (1,6):

    for j in range(1,6-i):
        print(" ",end=" ")

    
    for j in range(1,i+1):
        print(j,end=" ")

    for j in range(i-1,0,-1):
        print(j,end=" ")
    
    print()