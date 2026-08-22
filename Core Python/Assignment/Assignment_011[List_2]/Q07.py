# 7. Python Program to Find the Intersection of Two Lists

li = [10,20,30,40]
li2 = [30,40,50,60]

res = list(set(li) & set(li2))
print("Intersection of Two Lists:",res)