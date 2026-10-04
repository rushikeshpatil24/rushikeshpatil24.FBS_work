# Q4. Create a class College which has collection of students.
# Methods:
# a. Parameterized constructor for number of students
# b. AddStudent
# c. GetStudent
# d. RemoveStudent
# e. Override __str__ Method

class Student:
    def __init__(self, StudentId=0, Name="", Age=0, Percentage=0):
        self.StudentId = StudentId
        self.Name = Name
        self.Age = Age
        self.Percentage = Percentage

    def __str__(self):
        return f"{self.StudentId} {self.Name} {self.Age} {self.Percentage}%"


class College:
    def __init__(self, number_of_students):
        self.number_of_students = number_of_students
        self.students = []

    def AddStudent(self, student):
        if len(self.students) < self.number_of_students:
            self.students.append(student)
            print("Student added successfully.")
        else:
            print("College is full.")

    def GetStudent(self, StudentId):
        for student in self.students:
            if student.StudentId == StudentId:
                return student
        return None

    def RemoveStudent(self, StudentId):
        student = self.GetStudent(StudentId)
        if student is not None:
            self.students.remove(student)
            print("Student removed successfully.")
        else:
            print("Student not found.")

    def __str__(self):
        if not self.students:
            return "No students in college."

        result = "College Students:\n"
        for student in self.students:
            result += str(student) + "\n"
        return result


college = College(3)

s1 = Student(101, "Rishikesh", 21, 82.5)
s2 = Student(102, "Rahul", 20, 75.0)

college.AddStudent(s1)
college.AddStudent(s2)

print("\nAll Students:")
print(college)

print("Get Student:")
print(college.GetStudent(101))

college.RemoveStudent(102)

print("\nAfter Removing Student:")
print(college)
