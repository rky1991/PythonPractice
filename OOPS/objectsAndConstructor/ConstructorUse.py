class Person:
    def __init__(self):  # Constructor without parameters
        print("Constructor called!")
        self.name = "John"
        self.age = 30

    def __init__(self, name, salary):  # Parameterized constructor
        self.name = name
        self.salary = salary
        print("*****Constructor called!---->>>>"+name,salary)



    #Constructor will use while creating objectsAndConstructor
    #Constructor Overloading is not supported by Python
    # Can we have two constructor in same class ?
    #❌ No, Python does not support multiple constructors in the traditional way (like in Java or C++).
    #Only the second __init__ will be used.
    #The first one gets overwritten, and calling it like this:

#obj=Person() # ❌ This will throw: TypeError: __init__() missing 2 required positional arguments


obj=Person("Rahul",50000000)
print(obj)

