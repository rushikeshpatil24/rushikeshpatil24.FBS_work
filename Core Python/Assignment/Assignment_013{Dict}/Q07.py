# Q7. Python Program to Remove the Given Key from a Dictionary

dict = {1:'Rishikesh',2:'Nikita',3:'Om'}
def rem_key(dict):
    key = int(input("Enter key to remove:"))

    if key in dict:
        del dict[key]
        print(dict)
    else:
        print('given key is not exists in given dictionary')    


rem_key(dict)        