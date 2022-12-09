course = "learning java 😒😒😒"
upper_course = course.upper()
print(upper_course)
# calling upper() on string does not effect the original string
print("\n")
print(course)

# capitalize every first character of the string
print(course.title())

# capitalize first character of the string sentence
print(course.capitalize())

# find the index of the sequence of the characters
print(course.find("java"))
# replaces
print(course.replace("java", "Python"))
# check if character or sequence of character exist or not
print("java" in course)
