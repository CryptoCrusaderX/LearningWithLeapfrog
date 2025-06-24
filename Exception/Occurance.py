a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
try:
    c = a / b
    print("After diving we get", c)
except Exception as e:
    print(e)
    print("What displyed aboe is the type of error occurred.")
