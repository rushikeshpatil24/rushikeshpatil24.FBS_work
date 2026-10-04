# Q8. Python program to find all the anagrams and group them together
# from a given list of strings.

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

groups = {}

for word in words:
    key = ''.join(sorted(word))

    if key not in groups:
        groups[key] = []

    groups[key].append(word)

print("Anagram groups:")
for grp in groups.values():
    print(grp)
