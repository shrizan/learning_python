numbers = [1, 2, 3]
first = numbers[0]
second = numbers[1]
third = numbers[2]

# list unpacking
first, second, third = numbers
print(first)
print(second)
print(third)


numbers = [1, 2, 3, 5, 4, 56, 5, 3, 3]
first, second, *other = numbers
print(first)
print(second)
print(other)
