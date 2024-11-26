class Student:
    __name="Ravi" # Private Variable creation
    def __init__(self):
        print(self.__name)
        self.__display()

# Private Method
    def __display(self):
        print("Hello")

#can not access using Object
ob=Student()
