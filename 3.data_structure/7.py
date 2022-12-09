numbers = [1, 2, 10, 11, 3, 4, 5]
print(numbers.sort())  # none
print(numbers)  # sorted

# sorted does not affect the original list
sorted(numbers, reverse=True)

items = [
    ("Product1", 45),
    ("Product2", 100),
    ("Product3", 10)
]

print(sorted(items))


def sort_item(item):
    name, price = item
    return price


items.sort(key=sort_item)
print(items)
