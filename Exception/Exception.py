a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
try:
    c = a / b
    print("\nDividing a and b, we get:", c)
except:
    print("\nYou can't divide any number with 0")
    b = int(input("Enter the +ve value of b:"))
    print("\nNow, after diving we get", a / b)
else:
    print("\nNo exception, Now inside else")
    print("Product of a and b is", a * b)
finally:
    print("\nRegardless, Inside Finally")
    print("Sum of a and b is:", a + b)
