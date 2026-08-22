# 8. Print 1 to 100 in snakes and ladder pattern.

num = 1

for row in range(10):
    numbers = []
    
    for col in range(10):
        numbers.append(num)
        num += 1
        
    if row % 2 == 1:
        numbers.reverse()
    
    print(*numbers)
    