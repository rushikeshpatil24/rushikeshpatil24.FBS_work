# Generator which works like range()

def my_range(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0

    while (step > 0 and start < stop) or (step < 0 and start > stop):
        yield start
        start += step


for i in my_range(2, 10, 2):
    print(i)
