class Student:
    # Parametrize object
    def __init__(self, grade):
        self.__grade = grade

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, value):
        if 0 <= value <= 100:
            self.__grade = value
        else:
            print("Grade must be between 0 and 100")

s = Student(85)
print(s.grade)      # Uses the getter
s.grade = 92        # Uses the setter
print(s.grade)
s.grade = 150       # Invalid, won't change the grade
