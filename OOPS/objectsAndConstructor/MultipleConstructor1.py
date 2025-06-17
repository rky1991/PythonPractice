#Use a @classmethod as an alternative constructor

class Person:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_defaults(cls):
        return cls("John", 30000)

# Creating using standard constructor
p1 = Person("Alice", 70000)

# Creating using alternative constructor
p2 = Person.from_defaults()

print(p1.name, p1.salary)  # Alice 70000
print(p2.name, p2.salary)  # John 30000
