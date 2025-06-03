class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_vehicle_info(self):
        print(f"Vehicle Brand:{self.brand}, Model:{self.model}")


class Car(Vehicle):
    def __init__(self, brand, model, seating_capacity):
        super().__init__(brand, model)
        self.seat_capacity = seating_capacity

    def display_car_info(self):
        print(f"Car Seating Capacity:{self.seat_capacity}\n")


class Bike(Vehicle):
    def __init__(self, brand, model, engine_capacity):
        super().__init__(brand, model)
        self.engine_capacity = engine_capacity

    def display_bike_info(self):
        print(f"Bike Engine Capacity:{self.engine_capacity}CC")


# Example Usage
car = Car("Aston martin", "db707", 4)
bike = Bike("Triump", "400X", 400)

# Acessing the methods from different base and derived classes

car.display_vehicle_info()  # from vehicle
car.display_car_info()  # from car

bike.display_vehicle_info()  # from car
bike.display_bike_info()  # from bike
