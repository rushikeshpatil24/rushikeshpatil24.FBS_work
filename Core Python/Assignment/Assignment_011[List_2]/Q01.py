# 1. Python Program to Put Even and Odd elements of a List into two Different
# Lists

n =int(input('Enter the count of Element in list:'))
li=[]     #li=[0]* n
even_li=[]
odd_li=[]
for i in range(n):
    num=int(input(f'Enter the Element {i+1}:'))
    li.append(num)  #li[i] +=num

for i in range(n):
    if(li[i] % 2 ==0):
        even_li.append(li[i])
    else:
        odd_li.append(li[i])

print("All Elements of List:",li)
print("Even Elements of List:",even_li)
print("Odd elements of List:",odd_li)

