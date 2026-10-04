#### Q4. Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).

def square_of_key(num,dict={}):
    for i in range(1,num+1):
        dict[i]=i*i
    print(dict) 

square_of_key(7)       