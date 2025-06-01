class Car:
    def __init__(self, brand, color, speed=0):
        self.brand = brand
        self.color = color
        self.speed = speed

    def start(self):
        print(f"The {self.color} {self.brand} is starting")

    def accelrate(self, increase):
        self.speed += increase
        print(f"{self.brand} is now at {self.speed} km/h")


car1 = Car("Mercedes", "Black")
car2 = Car("Cadillac", "Blue")
car1.start()
car1.accelrate(40)
car2.accelrate(60)
