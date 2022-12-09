# lamda expression
items = [
    ("1", 100),
    ("2", 200),
    ("34", 34),
    ("55", 44)
]

items.sort(key=lambda item: item[1])
print(items)
