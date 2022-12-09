try:
    age = int(input("age: "))
    xFactor = 10/age
except (ValueError, ZeroDivisionError):
    print("Invalid age!!!")
else:
    print("Other error occurs")
