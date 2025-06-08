# Overloading Built-in methods
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    # Overloading built-in len() method/funtion using dunder method
    def __len__(self):
        return self.pages


book = Book("Norwegian Wood", 450)
print(len(book))
