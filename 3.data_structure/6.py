letters = ['a', 'b', 'c', 'd']
print(letters.index('a'))
# below code throws error
# print(letters.index('dd'))

if 'ee' in letters:
    print(letters.index('dd'))

print(letters.count('a'))
