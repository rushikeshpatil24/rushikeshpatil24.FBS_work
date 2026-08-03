# Q1. Write a program print following patterns :

for i in range(5):
    ch = 65  

    for j in range(i + 1):
        print(chr(ch), end=" ")
        ch += 1

    print()