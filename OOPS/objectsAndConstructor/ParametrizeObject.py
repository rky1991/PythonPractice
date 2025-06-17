class Employee:
    def __init__(self, name, salary):  # Parameterized constructor
        self.name = name
        self.salary = salary

# Creating objects with different values
emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 70000)

print(emp1.name, emp1.salary)  # Output: Alice 50000
print(emp2.name, emp2.salary)  # Output: Bob 70000
