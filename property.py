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

    # an price propery doing all the work here
    price = property(get_price, set_price)


p = Product(250)
print(p.price)
p.price = 750
print(p.price)
