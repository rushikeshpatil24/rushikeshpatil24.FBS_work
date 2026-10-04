#Q2.Python Program to Concatenate Two Dictionaries Into One.

def add_dic(dict1, dict2):
    dict1.update(dict2)
    return dict1
dict1 = {'Name': 'Rishiekesh'}
dict2 = {'Age': 21}
res = add_dic(dict1,dict2)
print(res)






