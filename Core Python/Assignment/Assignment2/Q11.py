## Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.

amt = int(input('Enter a Number:'))

notes_2000 = amt % 2000
amt = amt // 2000

notes_500 = amt % 500
amt = amt // 500

notes_100 = amt % 100
amt = amt // 100

notes_50 = amt % 50
amt = amt // 50

notes_20 = amt % 20
amt = amt // 20

notes_10 = amt % 10
amt = amt // 10

print('2000 Notes:',notes_2000)
print('500 Notes:',notes_500)
print('100 Notes:',notes_100)
print('50 Notes:',notes_50)
print('20 Notes:',notes_20)
print('10 Notes:',notes_10)
