class Employee:
    def __init__(self, name, department, salary):
        # Public Attribute
        self.name = name
        # Protected Attribute
        self._department = department
        # Private Attribute
        self.__salary = salary

    # Public Method
    def display_employee_details(self):
        return (
            f"Name:{self.name}\n"
            f"Department:{self._department}\n"
            f"Salary:{self.__salary}"
        )

    # Protected Method
    def _upgrade_department(self, new_department):
        if new_department:
            self._department = new_department
        else:
            raise ValueError("Department Name Can't Be Empty!")

    # Private Method
    def __validate_salary(self, salary):
        if salary <= 0:
            raise ValueError("Salary Must be positive!")

    # Public Property to access the private attribute
    @property
    def salary(self):
        return self.__salary

    # Setter Property to update the private attribute
    @salary.setter
    def salary(self, new_salary):
        self.__validate_salary(new_salary)
        self.__salary = new_salary

    def change_department(self, new_department):
        self._upgrade_department(new_department)
        print(f"Your Deparment Has Changed To {self._department.upper()}")


employee = Employee("Farwa", "Hiring Manager", 100000)

print(f"Employee Name:{employee.name}")
print(f"Employee Department:{employee._department}")

# Updating Protected attribute using public method
employee.change_department("Project Manager")

# Acessing and updating private attribute using @property Decorator
print(f"Initial Salary:रु {employee.salary}")
employee.salary = 2000000
print(f"Update Salary:रु {employee.salary}")

print("\nEmployee Details:")
print(employee.display_employee_details())
