def multiply(x, y):
    return x*y


print(multiply(2, 3))


def multi_multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multi_multiply(1, 2, 3, 4))
