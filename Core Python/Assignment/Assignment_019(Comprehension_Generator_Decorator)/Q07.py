# Find numbers from 1 to 1000 divisible by any single digit

result = [i for i in range(1, 1001)
          if any(i % d == 0 for d in range(1, 10))]

print(result)
