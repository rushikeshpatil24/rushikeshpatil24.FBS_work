#Q10.Write a program to reverse a number using recursion.

def  reverse(n,rev):
     
     if n > 0:
         d = n % 10
         n = n // 10
         rev = rev * 10 + d
         return reverse(n,rev)
     else:
         
         return rev
     
     
n = int(input("Enter Number:"))
rev = 0
res =  reverse(n,rev)
print("The Number is in Reverse Order:",res)