# Generator for palindrome numbers

def palindrome():
    n = 0

    while True:
        if str(n) == str(n)[::-1]:
            yield n
        n += 1


p = palindrome()

for i in range(20):
    print(next(p), end=" ")
