# def greet():
#     print("Hello World")
#
# greet()
#
# def greet_person(name):
#     print("Hello", name)
#
#
# greet_person("Daris")
# greet_person("Gent")


# def greet(name):
#     message=f"Hello,{name}"
#     print(message)
#
# greet("Alice")
# print(message)

# def greet(name):
#     message=f"{greeting},{name}"
#     print(message)
#
#
# greet("Bob")
# print(greeting)
#

# greeting="Hello"
#
#
# def greet():
#     global greeting
#     greeting="Goodbye"
#     name="Alice"
#
#
#     message=f"{greeting},{name}"
#
#     print(message)
#
#
# greet()
# print(greeting)

def greet_person(name,greeting="Hello"):
    message=f"{greeting},{name}"
    return message

print(greet_person("Alice"))
print(greet_person("Bob","Hi"))





