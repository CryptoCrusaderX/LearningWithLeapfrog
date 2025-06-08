# DuckTyping Example
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius


class Square:
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side * self.side


# This function doesn't care about the class unless it have a same methods
def print_area(shape):
    print(f"Area:{shape.calculate_area()}")


circle = Circle(8)
sqr = Square(5)
print_area(circle)
print_area(sqr)
