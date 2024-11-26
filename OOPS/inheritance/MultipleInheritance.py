
class A:
    def displayA(self):
        print("Hello")


class B:
    def displayB(self):
        print("Bye")

#Multiple Inheritance
class C(A,B):
    def displayC(self):
        print("Hi")



obj = C()
obj.displayA()
obj.displayB()
obj.displayC()