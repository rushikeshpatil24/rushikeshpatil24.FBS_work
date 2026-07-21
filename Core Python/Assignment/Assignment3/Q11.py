## Accept age of five people and also per person ticket amount and then calculate total amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

age1 = int(input("Enter age of first person :"))
tkprice1 = int(input("Enter the ticket price of first person :"))

total_price = 0

if (age1 < 12):
    total_price = total_price + (tkprice1 * 0.70)
elif (age1 > 59):
    total_price = total_price + (tkprice1 * 0.50)
else:
    total_price = total_price + tkprice1


age2 = int(input("Enter age of second person :"))
tkprice2 = int(input("Enter the ticket price of second person :"))

if (age2 < 12):
    total_price = total_price + (tkprice2 * 0.70)
elif (age2 > 59):
    total_price = total_price + (tkprice2 * 0.50)
else:
    total_price = total_price + tkprice2


age3 = int(input("Enter age of third person :"))
tkprice3 = int(input("Enter the ticket price of third person :"))

if (age3 < 12):
    total_price = total_price + (tkprice3 * 0.70)
elif (age3 > 59):
    total_price = total_price + (tkprice3 * 0.50)
else:
    total_price = total_price + tkprice3


age4 = int(input("Enter age of fourth person :"))
tkprice4 = int(input("Enter the ticket price of fourth person :"))

if (age4 < 12):
    total_price = total_price + (tkprice4 * 0.70)
elif (age4 > 59):
    total_price = total_price + (tkprice4 * 0.50)
else:
    total_price = total_price + tkprice4


age5 = int(input("Enter age of fifth person :"))
tkprice5 = int(input("Enter the ticket price of fifth person :"))

if (age5 < 12):
    total_price = total_price + (tkprice5 * 0.70)
elif (age5 > 59):
    total_price = total_price + (tkprice5 * 0.50)
else:
    total_price = total_price + tkprice5


print(f"Total price to pay for the trip of the five person : {total_price}")