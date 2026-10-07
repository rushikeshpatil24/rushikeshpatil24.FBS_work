# Count the length of each word using dictionary comprehension

s = input("Enter a sentence: ")

result = {i: len(i) for i in s.split()}

print(result)
