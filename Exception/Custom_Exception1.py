class NegativeError(Exception):
    def __init__(self, message):
        self.message = message


n = int(input("Enter a number to find factorial:"))
try:
    if n < 0:
        raise NegativeError("Negative Number don't have factorial!")
    else:
        f = 1
        for i in range(1, n + 1):
            f = f * i
        print(f"Factorial of {n} is {f}")

except NegativeError as ne:
    print("Exception Occured:", ne)
