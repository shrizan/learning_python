# sets
numbers = [1, 2, 2, 3, 4, 5, 1, 4]
uniques = set(numbers)
# set has all the list basic operation like insert remove append etc

first = {1, 2, 3, 4}
second = {3, 4, 5, 6}
union = first | second

print(union)

intersection = first & second
print(intersection)
# this gives differnce between two sets
print(first-second)

# semantric differnce (ie gives either in first or second not in both)
print(first ^ second)

print(1 in union)
