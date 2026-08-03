# Q1. Write a program print following patterns :

#  d  :

for i in range (1,6):

    for j in range(1,6-i):
        print(" ",end=" ")

    k=i
    for j in range(1,i+1):
        print(k,end=" ")
        k+=1

    k-=2
    for j in range(1,i):
        print(k,end=" ")
        k-=1
    
    print()
