# Prevent Inheriting the attributes
class MetaValidator(type):
    def __new__(mcs, name, bases, class_dict):
        # Skip validation for abstract classes
        if class_dict.pop("abstract", False):
            print(f"[Abstract Class] Skipping checks for: {name}")
            return super().__new__(mcs, name, bases, class_dict)

        # Validation: Class can't have both 'foo' and 'bar'
        if "foo" in class_dict and "bar" in class_dict:
            raise TypeError(f"'{name}' cannot define both 'foo' and 'bar'. Choose one.")

        # Validation: Must define at least one of 'foo' or 'bar'
        if "foo" not in class_dict and "bar" not in class_dict:
            raise TypeError(f"'{name}' must define either 'foo' or 'bar'.")

        print(f"[Valid Class] Class '{name}' passed all checks.")
        return super().__new__(mcs, name, bases, class_dict)


# Abstract base class — just a blueprint, not validated
class Base(metaclass=MetaValidator):
    abstract = True


# A valid class with only 'foo' defined
class FooClass(metaclass=MetaValidator):
    foo = 100  # Just a dummy attribute to pass the metaclass check
