# Base class for handling food types
class FoodType(object):
    events = []  # Keeps track of all food type instances

    def __init__(self, ftype, items):
        self.ftype = ftype
        self.items = items
        FoodType.events.append(self)  # Register each instance in the events list

    def run(self):
        print(f"Food Type: {self.ftype}")
        print("Food Menu:", self.items)

    @staticmethod
    def run_events():
        # Loop through all registered food types and print their info
        for event in FoodType.events:
            event.run()


# Function to dynamically create subclasses of FoodType
def sub_food(ftype):
    class_name = ftype.capitalize()

    # Custom constructor for the dynamic subclass
    def __init__(self, items):
        # Call parent constructor with the given food type
        FoodType.__init__(self, ftype, items)

    # Dynamically create the class and assign it to global namespace
    globals()[class_name] = type(class_name, (FoodType,), {"__init__": __init__})


# Execution block
if __name__ == "__main__":
    food_types = ["Vegetarian", "Nonvegetarian"]

    # Dynamically create subclasses based on food_types list
    [sub_food(ftype) for ftype in food_types]

    # Create instances using the newly defined dynamic classes
    Vegetarian(["Spinach", "Bitter Gourd"])
    Nonvegetarian(["Meat", "Fish"])

    # Run the event to print food details
    FoodType.run_events()
