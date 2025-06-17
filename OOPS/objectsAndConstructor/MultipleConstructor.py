class Person:
    def __init__(self, name="John", salary=30000):
        self.name = name
        self.salary = salary

# You can use default arguments or class methods to simulate this behavior.


# Both work:
p1 = Person()                        # Uses default values
p2 = Person("Alice", 50000)         # Uses provided values
p3 = Person("Rahul", 60000)

print(p1.name, p1.salary)  # John 30000
print(p2.name, p2.salary)  # Alice 50000
print(p3.name, p3.salary)  # Alice 60000
