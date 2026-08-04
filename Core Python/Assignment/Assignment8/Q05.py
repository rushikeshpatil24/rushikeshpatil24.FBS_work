# Q5.Sum of all prime numbers between 1 to n.

def primeNo(num):
    total = 0

    for i in range(2, num + 1):
        isPrime = True

        for j in range(2, i):
            if i % j == 0:
                isPrime = False
                break

        if isPrime:
            total += i

    return total

num = int(input("Enter Number: "))

result = primeNo(num)
print("Sum of all Prime Numbers is:", result)