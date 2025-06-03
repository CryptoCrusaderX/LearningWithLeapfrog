class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_personal_info(self):
        print(f"Name:{self.name}, Age:{self.age}")


class Employee(Person):
    def __init__(self, name, age, employee_id, Department):
        super().__init__(name, age)
        self.department = Department
        self.employee_id = employee_id

    def display_employee_info(self):
        print(f"Employee Id:{self.employee_id}, Department:{self.department}")


class Manager(Employee):
    def __init__(self, name, age, employee_id, Department, team_size):
        super().__init__(name, age, employee_id, Department)
        self.team_size = team_size

    def display_manager_info(self):
        print(f"Manager of Department:{self.department}, Team Size:{self.team_size}")


# Example Usage

manager = Manager("Sarad", 45, "E05", "IT", 10)
# Acessing methods from all levels
manager.display_personal_info()
manager.display_employee_info()
manager.display_manager_info()
