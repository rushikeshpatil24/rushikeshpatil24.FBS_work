# Q2. Python program to remove the intersection of a second set with a first set.

s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}

s1.difference_update(s2)
print("First set after removing intersection:", s1)
