# Q2.Write a program to find the maximum and minimum element in a list.

li = [2,40,60,20,110,46,86]
max = li[0]
min =li[0]

for val in range(1,len(li)):
    if(li[val] > max):
        max = li[val]


for val in range(0,len(li)):
    if li[val] < min:
        min = li[val]
        
print("Maximum Element is:",max)
print("Minimum Element is:",min)