point = (1, 2)
print(type(point))
# does not require to include parenthesis
point = 1, 2
print(type(point))
point = 1,
print(type(point))
point = ()
print(type(point))
# above all are tuple
print(point+(3, 4))
print((1, 2)*3)
print((1, 2)+(3, 4))
print(tuple([1, 2]))
print(tuple("hello wold"))

print((1, 2, 3, 4, 5)[1:3])  # returns another tuple
# tuples are immutable
