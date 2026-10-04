# Q6. Python program to find the two numbers whose product is maximum
# among all the pairs in a given list of numbers. Use Python set.

num = [-10, -3, 5, 6, 2, 8]

pairs = set()

for i in range(len(num)):
    for j in range(i + 1, len(num)):
        pairs.add((num[i], num[j]))

max_pair = max(pairs, key=lambda pair: pair[0] * pair[1])

print("Two numbers:", max_pair)
print("Maximum product:", max_pair[0] * max_pair[1])
