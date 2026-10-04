# Q5. Python program to find the longest common prefix of all strings. Use Python set.

str = ["flower", "flow", "flight"]

prefix = ""

for i in range(len(str[0])):
    chars = {word[i] for word in str if i < len(word)}

    if len(chars) == 1:
        prefix += str[0][i]
    else:
        break

print("Longest common prefix:", prefix)
