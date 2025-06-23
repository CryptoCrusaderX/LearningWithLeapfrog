a = int(input("Enter a value of a:"))
b = int(input("Enter a value of b:"))

try:
    c = a / b
    print("After division we get:", c)
except:
    print("Exception Occured")
else:
    print("Exception Not Occured")
finally:
    print("Inside Finally")
    print("Code of this parts always runs")
