class tooyoungerror(Exception):
    def __init__(self, message):
        self.message = message


class tooolderror(Exception):
    def __init__(self, message):
        self.message = message


age = int(input("Enter your age:"))
try:
    if age < 18:
        raise tooyoungerror("You're too young to get married!")
    elif age > 60:
        raise tooolderror("You're too old to get married!")
    else:
        print("We will find you a perfect match!")
except Exception as e:
    print("Exception Occured:", e)
