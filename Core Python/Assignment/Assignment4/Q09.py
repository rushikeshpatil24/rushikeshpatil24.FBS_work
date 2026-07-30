# Q9. Write a program to print all numbers in a range divisible by a given number.

start = int(input("Enter start: "))
end = int(input("Enter end: "))
d = int(input("Enter divisor: "))

for i in range(start, end + 1):
    if i % d == 0:
        print(f"These numbers are divisible by:{i}")