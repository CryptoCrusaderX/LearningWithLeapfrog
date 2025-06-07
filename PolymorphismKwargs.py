# Using **kwargs for keyword arguments
class Greeting:
    def say_hello(self, **kwargs):
        if "name" in kwargs:
            return f"Hello,{kwargs['name']}!"
        return "Hello Stranger"


greet = Greeting()
print(greet.say_hello())
print(greet.say_hello(name="John Doe"))
