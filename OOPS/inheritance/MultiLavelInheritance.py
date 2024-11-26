class A:
    def displayA(self):
        print("Hello")


class B(A):
    def displayB(self):
        print("Bye")

class C(B):
    def displayC(self):
        print("Hi")



obj = C()
obj.displayA()
obj.displayB()
obj.displayC()