# Q2. Enter number of students from user.
# For those many students accept marks of 5
# subject marks from user and calculate percentage.
# Display all percentage and average percentage of students.
   
students = int(input('Enter number of Student:'))
total_per= 0

for i in range(1, students + 1):
    print("\nEnter marks of Student",i)
    
    total = 0
    
    for j in range(1,6):
        marks = int(input(f'Subject {j} Marks:'))
        total += marks
        
    percentage = (total / 500) * 100
    print('Percentage is :',percentage)
    
    total_per += percentage
average_per = total_per / students

print("\nAverage Percentage of students :",average_per)
