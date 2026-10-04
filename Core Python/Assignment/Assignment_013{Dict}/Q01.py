#Q1.Python Program to Add a Key-Value Pair to the Dictionary.

def student(**args):
    dict={args['Name']:args['Age']}
    return dict
res = student(Name = "Rishikesh", Age = 21)
print(res)



