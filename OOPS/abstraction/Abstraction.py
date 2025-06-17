#ABC is predefined abstract class , required to extend to make any class abstract
from abc import ABC,abstractmethod


class A(ABC):
     @abstractmethod
     def display(self): # Abstract Method
         None

class B(A):
    def display(self):
        print("This is Display Method: ")


ob = B()
ob.display()

# Can not instansiate a class
#ob1 = A()
#ob1.display()