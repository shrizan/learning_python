items = [
    ("Product1", 45),
    ("Product2", 100),
    ("Product3", 10)
]

products_greater_than_10 = list(filter(lambda item: item[1] > 10, items))
print(products_greater_than_10)
