#ABC is predefined abstract class , required to extend to make any class abstract
from abc import ABC,abstractmethod


class A(ABC):
     @abstractmethod
     def display(self): # Abstract Method
         None

     @abstractmethod
     def display1(self):  # Abstract Method
         pass

     @abstractmethod
     def display2(self):  # Abstract Method
         pass

class B(A):
    def display(self):
        print("This is Display Method: ")

    def display1(self):
        print("This is Display1 Method:---->>> ")


class C(B):
    def display2(self):
        print("This is Display 2 Method: <<<<------- ")
#ypeError: Can't instantiate abstract class A with abstract methods display, display1, display2
#ob = A() --> Can not create object for this class , All abstract method not got implementatin
#ob = B() --> Can not create object for this class ,
ob= C()
ob.display()
ob.display1()
ob.display2()
