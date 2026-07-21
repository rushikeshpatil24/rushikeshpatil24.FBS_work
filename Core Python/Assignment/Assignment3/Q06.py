## Write a program to check Profit or Loss.

cost_p = float(input('Enetr Cost Price:'))
selling_p = float(input('Enter Selling Price:'))

if(selling_p > cost_p):
    print('Profit')
elif(cost_p > selling_p):
    print('Loss')
else:
    print('No Profit No Loss')