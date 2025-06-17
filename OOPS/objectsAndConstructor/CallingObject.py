class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

c1 = Circle(5)
print("Area:", c1.area())           # Output: Area: 78.5
print("Perimeter:", c1.perimeter()) # Output: Perimeter: 31.400000000000002
