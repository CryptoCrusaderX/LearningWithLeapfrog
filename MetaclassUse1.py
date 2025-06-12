class CustomAttributeChecker(type):
    def __new__(metacls, class_name, base_classes, class_attrs):
        # If both 'foo' and 'bar' are in the class, that's not allowed.
        # We want only one of them, not both.
        if "foo" in class_attrs and "bar" in class_attrs:
            raise TypeError(
                f"Oops! Class '{class_name}' can't have both 'foo' and 'bar'. Pick one."
            )

        # If neither 'foo' nor 'bar' is there, that's also a problem.
        # The class has to define at least one of them.
        if "foo" not in class_attrs and "bar" not in class_attrs:
            raise TypeError(
                f"Hey! Class '{class_name}' needs to define either 'foo' or 'bar'."
            )

        # If the class has either 'foo' or 'bar' (but not both), it's good to go.
        print(f"Nice! '{class_name}' was created correctly.")

        # This actually creates the class and returns it.
        return super().__new__(metacls, class_name, base_classes, class_attrs)


# Now we make a class that uses our custom metaclass.
class MyCustomClass(metaclass=CustomAttributeChecker):
    # Try commenting out one of these lines to test the rules above.
    foo = 42
    bar = 34  # Having both 'foo' and 'bar' will trigger an error!


# This line tries to make an object of the class.
# But because both attributes are defined, it will raise an error.
instance = MyCustomClass()
