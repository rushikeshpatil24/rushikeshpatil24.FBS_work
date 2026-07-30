#Q5.Write a program to print prime numbers between 1 to 100.

start = int(input("Enter starting No :"))
end = int(input("Enter End No :"))
print("The Prime no in given range is ")

for num in range(start , end):

    if ( num > 1 ):

        for i in range (2, num):    
            if (num % i == 0):
                break 
        else:
            print(num)

    else:
        print("The number is not prime or Composite :",num)