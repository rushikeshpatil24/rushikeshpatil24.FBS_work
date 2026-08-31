# 1. A list contains the denominations as follows :
# D = [2000, 500, 200, 100 , 50, 20, 10, 5]
# Accept an amount from user and calculate how many
# minimum number of notes will be needed for that
# amount.

D = [2000, 500, 200, 100 , 50, 20, 10, 5]

amount = int(input("Enter Amount:"))

count = 0

for note in D:
    count += amount // note
    amount = amount % note
    
if amount != 0:
    print("Amount can not be exactly")
else:
    print("Minimun number of notes:",count)