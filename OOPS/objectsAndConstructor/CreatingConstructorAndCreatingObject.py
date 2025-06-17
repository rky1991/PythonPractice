class Person:
    def __init__(self):  # Constructor without parameters
        print("Constructor called!")
        self.name = "John"
        self.age = 30


# No Argumnet Constructor
obj=Person()
print(obj)

p1 = Person()  # Object created, constructor automatically called
print(p1.name)  # Output: John
print(p1.age)   # Output: 30


