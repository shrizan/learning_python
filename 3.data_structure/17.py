from array import array
items = array("i", [1, 2, 3, 4, 5])
for item in items:
    print(item)

items.append(6)
items.insert(0, 11)
items.pop()
items.remove(5)
