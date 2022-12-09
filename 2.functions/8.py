def testMe(input):
    if input % 3 == 0:
        return "Fizz"
    elif input % 5 == 0:
        return "Buzz"
    elif input % 3 == 0 and input % 5 == 0:
        return "FizzBuzz"
    return input


print(testMe(5))
print(testMe(3))
print(testMe(15))
print(testMe(11))
