from abc import ABC, abstractmethod


# Abstract class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


# Child class inheriting abstract parent class
class Dog(Animal):
    def sound(self):
        return "Bark"


class Cat(Animal):
    def sound(self):
        return "Meow"


#
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.sound())
