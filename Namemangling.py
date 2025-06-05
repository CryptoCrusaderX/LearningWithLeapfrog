class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price


product = Product("Cetaphil", 1750)

print(product._Product__name)
print(product._Product__price)
