### Write a program to calculate the percentage of student based on maarks of any 5 subjects

#take input for 5 subjects

m1 = int(input('Enter Math Marks:'))
m2 = int(input('Enter  English Marks:'))
m3 = int(input('Enter  Science Marks:'))
m4 = int(input('Enter  Pyrhon Marks:'))
m5 = int(input('Enter  Java Marks:'))

#calculate Obtained Marks

obtain_marks = m1 + m2 + m3 + m4 + m5
percentage = (obtain_marks / 500) * 100

print("Percentage of 5 Subjects:",percentage)