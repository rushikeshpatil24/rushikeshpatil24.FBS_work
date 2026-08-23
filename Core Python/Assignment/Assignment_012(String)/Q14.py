#Q14.Python Program to count the occurrences of ach word in a string.

string = input("Enter a string: ")

words = string.split()
count = {}

for word in words:
    count[word] = count.get(word, 0) + 1

print("Word occurrences:")
for word,frequency in count.items():
    print(word, ":",frequency)