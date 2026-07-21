## Write a program to calculate selling price of a book  based on cost price and discount.

cost_p = int(input('Enter Cost price:'))
discount = float(input('Enter Discount:'))

discount = (cost_p * discount) / 100
selling_p = cost_p - discount

print('Given Discount is',discount)
print('Selling Price is:',selling_p)