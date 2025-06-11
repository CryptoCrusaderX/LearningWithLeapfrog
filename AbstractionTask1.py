from abc import ABC, abstractmethod


class Library(ABC):
    @abstractmethod
    def add_book(bookname):
        pass

    def borrow_book(bookname):
        pass

    def return_book(bookname):
        pass

    def display_book(bookname):
        pass


class PublicLibrary(Library):

    def __init__(self):
        self.avialable_books = []
        self.borrowed_books = []

    def add_book(self, bookname):
        if isinstance(bookname, str):
            self.avialable_books.append(bookname)
            print(f"Book name {bookname.upper()} has been added to the Library")
        else:
            print("Please Enter a Book Name")

    def borrow_book(self, bookname):
        if isinstance(bookname, str):
            if bookname in self.avialable_books:
                self.borrowed_books.append(bookname)
                self.avialable_books.remove(bookname)
                print(
                    f"\nThank You for borrowing book from us!\n"
                    f"Book Name:{bookname.upper()}"
                )
            else:
                print("\nThe books you've asked for is avilable at the moment:)")
        else:
            print("Please Enter a book name!")

    def return_book(self, bookname):
        if isinstance(bookname, str):
            if bookname in self.borrowed_books:
                self.borrowed_books.remove(bookname)
                self.avialable_books.append(bookname)
                print(
                    f"\nThank You for returning the book!\n"
                    f"Book Name:{bookname.upper()}"
                )
            else:
                print("\nThis books doesn't belongs to this library!")
        else:
            print("Please Enter a book name!")

    def display_book(self):
        print("\nAll the avialbe books in this libray are:")
        print(self.avialable_books)


libraria = PublicLibrary()
libraria.add_book("Python 101")
libraria.add_book("Data Structures")
libraria.add_book("Machine Learning")
libraria.display_book()

libraria.borrow_book("Machine Learning")

libraria.return_book("Kafka on the shore")
libraria.borrow_book("The Idiot")
libraria.return_book("Machine Learning")
