# Dictionaries
point = {"x": 1, "y": 2}
# this approach is cleaner than the first one
point = dict(x=1, y=2)
print(point["x"])
point["x"] = 10
print(point["x"])
point["z"] = 1000
print(point)
if "n" in point:
    print["n"]
print(point.get("g", 2000))
# delete item from dictionary
del point["x"]
print(point)

for key in point:
    print(key, point[key])

for key, value in point.items():
    print(key, value)
