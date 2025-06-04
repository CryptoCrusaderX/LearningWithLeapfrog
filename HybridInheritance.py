class Person:

    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Name:{self.name}")


class Student(Person):
    def __init__(self, name, student_id):
        Person.__init__(self, name)
        self.student_id = student_id

    def display(self):
        super().display()
        print(f"Student ID:{self.student_id}")


class Teacher(Person):
    def __init__(self, name, subject):
        Person.__init__(self, name)
        self.subject = subject

    def display(self):
        super().display(self)
        print(f"Teaches: {self.subject}")


class TeachingAssitant(Teacher, Student):
    def __init__(self, name, student_id, subject):
        Student.__init__(self, name, student_id)
        Teacher.__init__(self, name, subject)

    def display(self):
        print("Teaching Assistand Info:")
        Student.display(self)
        print(f"Also assists in subject: {self.subject}")


taa = TeachingAssitant("Farwa", 260112, "Operating System")
taa.display()
