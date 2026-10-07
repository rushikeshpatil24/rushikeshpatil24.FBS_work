# Memoization decorator

def memoize(fun):
    cache = {}

    def inner(n):
        if n not in cache:
            cache[n] = fun(n)
        return cache[n]

    return inner


@memoize
def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)


n = int(input("Enter number: "))
print("Factorial:", fact(n))
