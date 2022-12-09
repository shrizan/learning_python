# ** in variable allows us to pass multiple key value pair and python wraps it to dictionary
def save_user(**user):
    print(user)


save_user(name="Python", age=40)
