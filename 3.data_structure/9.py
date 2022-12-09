items = [
    ("Product1", 45),
    ("Product2", 100),
    ("Product3", 10)
]

prices = []
for item in items:
    prices.append(item[1])

print(prices)

x = list(map(lambda item: item[1], items))
print(x)
