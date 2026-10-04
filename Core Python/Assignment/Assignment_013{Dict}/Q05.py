#### Q5. Python Program to Sum All the Items in a Dictionary.

dict = {'a':20,'b':40,'c':60}

def add_values(dict):

    li = dict.values()
    count = 0
    for i in li:
        count += i
    return count   

res = add_values(dict)
print("Sum All the items in a Dictionary:",res)