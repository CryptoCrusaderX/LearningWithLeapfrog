# Using *args for variaable lenght arguments.
class Calculator:
    def add(self, *args):
        return sum(args)


calc = Calculator()
print(calc.add(10))
print(calc.add(10, 12))
print(calc.add(10, 24, 36))
