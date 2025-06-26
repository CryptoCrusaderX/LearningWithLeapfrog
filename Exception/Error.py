n = int(input("Enter number between 1 to 5:"))
a = [3, 4, 5, 6, "8"]
try:
    sum = 0
    for i in range(n):
        sum = sum + a[i]
    print("Inside Try!")
    print("Sum of the index is ", sum)
except:
    sum = 0
    for i in range(n):
        sum = sum + int(a[i])
    print("Inside Except")
    print("Sum to that index is", sum)
