# Q8.Write a program to find which numbers are divisible by 7 and multiply of 5 in a given range.

start = int(input("Enter start: "))
end = int(input("Enter end: "))

for i in range(start, end + 1):
    if i % 7 == 0 and i % 5 == 0:
        print('These numbers are divisible by 7 and multiply by 5:',i)