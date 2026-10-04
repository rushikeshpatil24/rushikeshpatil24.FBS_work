# Q9. Python program to find all the unique combinations of 3 numbers
# from a given list of numbers, adding up to a target number.

num = [1, 2, 3, 4, 5, 6]
target = 10

combinations = set()

for i in range(len(num)):
    for j in range(i + 1, len(num)):
        for k in range(j + 1, len(num)):
            if num[i] + num[j] + num[k] == target:
                combinations.add((num[i], num[j], num[k]))

print("Unique combinations:", combinations)
