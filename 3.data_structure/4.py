letters = ['x', 'y', 'z']
for letter in letters:
    print(letter)


# enumerate returns tuple first index and second item
for index, letter in enumerate(letters):
    print(f"{index}:{letter}")
