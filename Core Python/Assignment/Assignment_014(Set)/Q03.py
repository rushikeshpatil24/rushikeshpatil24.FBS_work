# Q3. Python program to find all the unique words and count the frequency
# of occurrence from a given list of strings. Use Python set data type.

words = ["python", "java", "python", "c", "java", "python"]

unique_words = set(words)

for word in unique_words:
    print(word, ":", words.count(word))
