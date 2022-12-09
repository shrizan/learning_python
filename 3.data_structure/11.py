# list comprehension
items = [
    ("Product1", 45),
    ("Product2", 100),
    ("Product3", 10)
]

# [expression for item in items]
prices = list(item[1] for item in items)

# filte using list comprehension
filtered = list([item[1] for item in items if item[1] > 10])
print(filtered)
