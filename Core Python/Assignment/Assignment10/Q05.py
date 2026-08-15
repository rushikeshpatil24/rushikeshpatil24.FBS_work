# Q5.Accept a number from the user and check if this element is present in the list or not. Also tell how many times it is present in the list.

num = int(input("Enter Number:"))

li = [10,24,40,60,24,32,98]
 
if num in li:
     print("Element present in list")
     print("Number of times present:",li.count(num))
else:

     print("element not found")