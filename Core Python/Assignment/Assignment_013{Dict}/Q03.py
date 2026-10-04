#Q3.Python Program to Check if a Given Key Exists in a Dictionary or Not

def iskey_exicts(dic,key):

    if key in dic:
        return f"Given key: {key} exists in given Dictionary"
    else:
        return f"Given key: {key} dose not exists in given Dictionary"
    
dic = {'Rishikesh':21, 'Siddhu':22}
res = iskey_exicts(dic,'Om')
print(res)
    
    
    
    
    
  
