class Engine:
    def start_engine(self):
        print("Engine Started!")


class Wheels:
    def rotate(self):
        print("Wheels are rotating.")


class Car(Engine, Wheels):
    pass


car = Car()
car.start_engine()
car.rotate()
