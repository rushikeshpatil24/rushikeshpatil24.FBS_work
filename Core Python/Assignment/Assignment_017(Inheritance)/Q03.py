# Q3. Create a class MedicalStudent inherited from Student with
# Specialization and MarksOfInternship.
# Methods: Parameterized constructor, Display, Accept,
# override CalculateRank and override __str__ method.

class Student:
    def __init__(self, StudentId=0, Name="", Age=0, Percentage=0):
        self.StudentId = StudentId
        self.Name = Name
        self.Age = Age
        self.Percentage = Percentage

    def Display(self):
        print("Student ID:", self.StudentId)
        print("Name:", self.Name)
        print("Age:", self.Age)
        print("Percentage:", self.Percentage)
        print("Rank:", self.CalculateRank())

    def Accept(self):
        self.StudentId = int(input("Enter Student ID: "))
        self.Name = input("Enter Name: ")
        self.Age = int(input("Enter Age: "))
        self.Percentage = float(input("Enter Percentage: "))

    def CalculateRank(self):
        if self.Percentage >= 75:
            return "Distinction"
        elif self.Percentage >= 60:
            return "First Class"
        elif self.Percentage >= 50:
            return "Second Class"
        elif self.Percentage >= 40:
            return "Pass"
        else:
            return "Fail"

    def __str__(self):
        return f"{self.StudentId} {self.Name} {self.Age} {self.Percentage}"


class MedicalStudent(Student):
    def __init__(self, StudentId=0, Name="", Age=0, Percentage=0,
                 Specialization="", MarksOfInternship=0):
        super().__init__(StudentId, Name, Age, Percentage)
        self.Specialization = Specialization
        self.MarksOfInternship = MarksOfInternship

    def Display(self):
        super().Display()
        print("Specialization:", self.Specialization)
        print("Marks Of Internship:", self.MarksOfInternship)

    def Accept(self):
        super().Accept()
        self.Specialization = input("Enter Specialization: ")
        self.MarksOfInternship = float(input("Enter Marks Of Internship: "))

    def CalculateRank(self):
        if self.Percentage >= 75:
            return "Distinction"
        elif self.Percentage >= 60:
            return "First Class"
        elif self.Percentage >= 50:
            return "Second Class"
        elif self.Percentage >= 40:
            return "Pass"
        else:
            return "Fail"

    def __str__(self):
        return (f"{self.StudentId} {self.Name} - {self.Age}  "
                f"{self.Percentage} {self.Specialization} "
                f"{self.MarksOfInternship}")


m1 = MedicalStudent(101, "Rishikesh", 21, 82.5, "Cardiology", 90)
m1.Display()
print(m1)
