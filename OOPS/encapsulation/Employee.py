class Employee:
    def __init__(self, name, salary):
        self.name = name          # public attribute
        self.__salary = salary    # private attribute Defined using double underscore __ before the variable or method name.

    def get_salary(self):
        return self.__salary

    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary amount")

emp = Employee("John", 50000)
print(emp.name)            # Allowed
print(emp.get_salary())    # Accessing private variable via getter

emp.set_salary(60000)      # Modifying private variable via setter
print(emp.get_salary())

# Direct access will raise AttributeError
#print(emp.__salary)     # Uncommenting this will cause an error
