# An sigle function showing diff behaviour(polymorphism) with typechecking
class Printer:
    def print_data(self, data):
        if isinstance(data, int):
            return f"Printing Integer:{data}"
        elif isinstance(data, str):
            return f"Printing String:{data}"
        elif isinstance(data, float):
            return f"Printing Float Value:{data}"
        else:
            return


printer = Printer()
print(printer.print_data(101))
print(printer.print_data(10.001))
print(printer.print_data("SARAD"))
print(printer.print_data([23, "kk", 11]))
