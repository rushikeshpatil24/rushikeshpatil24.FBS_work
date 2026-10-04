# Q7. Given two sets of numbers, find the missing numbers in the second set
# as compared to the first and vice versa. Use Python set.

s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}

missing_in_second = s1 - s2
missing_in_first = s2 - s1

print("Numbers missing in second set:", missing_in_second)
print("Numbers missing in first set:", missing_in_first)
