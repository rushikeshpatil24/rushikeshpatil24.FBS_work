# Q13.Write a program to print the list after removing even numbers.

li = [7,57,6,46,89,2,82,85,76,56,5,9,83]
li2 = []
for i in range(len(li)):
    if (li[i] % 2 != 0):
        li2.append(li[i])
    
print("List after removing Even Elements :",li2)
