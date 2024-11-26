class A:
    def displayA(self):
        print("Hello")


class B(A):
    def displayB(self):
        print("Bye")


obj = B()
obj.displayA()
obj.displayB()
