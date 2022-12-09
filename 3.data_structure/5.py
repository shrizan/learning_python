numbers = [1, 2, 3, 4, 5]
numbers.append(6)  # adds number at end of the list
print(numbers)
numbers.insert(0, 66)
print(numbers)

# remove from last
numbers.pop()  # removes 6
print(numbers)

# remove value from index 0
numbers.pop(0)
print(numbers)

# remove by items value
numbers.remove(2)

# remove range of items
del numbers[0:1]

# delete all the items
numbers.clear()
