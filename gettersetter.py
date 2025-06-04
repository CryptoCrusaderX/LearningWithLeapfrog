class Product:
    def __init__(self, price):
        self.__price = price

    # an getter method to get private attribute from outside of the class
    def get_price(self):
        return self.__price

    # an setter method to set private attribute from outside of the class
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            raise ValueError("Price Must be Positive!")


p = Product(100)

# getting an private attribute from outside of the class
print(p.get_price())

# setting an private attribute from outside of the class
p.set_price(500)
print(p.get_price())
