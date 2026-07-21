## Write  a program to calculate total salary of employee based on basic , da=10% of basic,ta=12% of basic,hra=15% of basic.

basic_salary = int(input('Enter Basic salary:'))

da = (basic_salary * 10) / 100
ta = (basic_salary * 12) / 100
hra = (basic_salary * 15) / 100

total_salary = basic_salary + da + ta + hra

print('Da=',da)
print('Ta=',ta)
print('HRA=',hra)
print('Total salary of Employee is:',total_salary)