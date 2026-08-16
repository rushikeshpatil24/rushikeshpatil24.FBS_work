# Q9.Write a program having n number of elements in the list and find out even and odd elements in that list,
# and then create two separate lists which will have even elements and other will have odd elements.

li = [7,57,6,46,89,2,7,82,7,85,76,56,5,7,9,83]
li2 = []
li3 = []
for i in range(len(li)):
    if (li[i] % 2 == 0):
        li2.append(li[i])
    else:
        li3.append(li[i])

print("Even Elements:",li2)
print("Odd Elements:",li3)