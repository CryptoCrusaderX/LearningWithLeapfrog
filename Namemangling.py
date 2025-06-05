class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price


product = Product("Cetaphil", 1750)
# Acessing Private attribute from outside of the class only with the help of NAME MANGLING
print(product._Product__name)
print(product._Product__price)
