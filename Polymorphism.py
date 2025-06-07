class Dog:

    def speak(self):
        return "Bark!"


class Cat:
    def speak(self):
        return "Meow!"


def animal_sound(animal):
    print(animal.speak())


cat = Cat()
dog = Dog()

animal_sound(dog)
animal_sound(cat)
