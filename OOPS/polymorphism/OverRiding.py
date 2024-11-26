class A:
    def showData(self):
        print("Hello, i am in A")
class B(A):
    def showData(self):
        print("Hello i am in B")

ob= B()
ob.showData()