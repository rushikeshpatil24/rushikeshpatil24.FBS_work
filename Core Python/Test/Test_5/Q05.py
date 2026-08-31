# 5. Python Program to Find the Union of two Lists without
# using set concept.

l1 = [10,20,30,40]
l2 = [30,40,50,60]
l3 = []

for val in l1:
    if val not in l3:
        l3.append(val)
        
for val in l2:
    if val not in l3:
        l3.append(val)
        
print("Union of two Lists:",l3)