# Student contains SYMARKS and TYMARKS objects

from SY.symarks import SYMARKS
from TY.tymarks import TYMARKS


class Student:
    def __init__(self, rollno, name, symarks, tymarks):
        self.rollno = rollno
        self.name = name
        self.symarks = symarks
        self.tymarks = tymarks

    def total(self):
        return (self.symarks.computer + self.symarks.maths +
                self.symarks.electronics + self.tymarks.theory +
                self.tymarks.practical)

    def grade(self):
        marks = self.total()

        if marks >= 350:
            return "A"
        elif marks >= 300:
            return "B"
        elif marks >= 250:
            return "C"
        elif marks >= 200:
            return "Pass Class"
        else:
            return "Fail"

    def display(self):
        print("Roll No:", self.rollno)
        print("Name:", self.name)
        print("Computer:", self.symarks.computer)
        print("Maths:", self.symarks.maths)
        print("Electronics:", self.symarks.electronics)
        print("Theory:", self.tymarks.theory)
        print("Practical:", self.tymarks.practical)
        print("Total:", self.total())
        print("Grade:", self.grade())


sy = SYMARKS(70, 65, 60)
ty = TYMARKS(75, 80)

s = Student(101, "Rishikesh", sy, ty)
s.display()
