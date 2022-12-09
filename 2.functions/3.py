def get_greeting(name):
    return f"Hi! {name}"


message = get_greeting("Java")
print(message)


def does_not_return():
    print("This does not return")


print(does_not_return())  # None
