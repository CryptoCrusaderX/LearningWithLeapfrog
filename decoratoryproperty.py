class Product:
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            raise ValueError("Price Must be Positive!")


product = Product(100)
# property decorator made getting and setting the value of price possible which is an private attribute
print(product.price)
product.price = 400
print(product.price)
