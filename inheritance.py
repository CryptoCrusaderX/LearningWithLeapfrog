class LibraryMember:
    def __init__(self, name, membership_id):
        self.name = name
        self.membership_id = membership_id

    def borrow_book(self):
        print(f"{self.name} with membership Id:{self.membership_id} has borrowed book")

    def return_book(self):
        print(f"Thank you for returning the book, {self.name}:)")


class StudentMember(LibraryMember):
    def __init__(self, name, membership_id, student_id):
        super().__init__(name, membership_id)
        self.student_id = student_id

    def borrow_book(self):
        print(f"Your Student Id is:{self.student_id}")
        print(super().borrow_book())

    def access_study_room(self):
        print("Student now have an access to the study room")
        print("Student details:")
        print(f"Student name:{self.name}")
        print(f"Student Membership Id:{self.membership_id}")
        print(f"Student Id:{self.student_id}")


l1 = LibraryMember("Farwa", "007")
l1.borrow_book()
l1.return_book()

s1 = StudentMember("Farwa", "007", 250112)
s1.borrow_book()
s1.access_study_room()
