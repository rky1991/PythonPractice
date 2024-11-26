class Demo:
     a=10
     def sum(self):
         print(self.a) # always use self keword before
         #print(a) ## directly we can not use a variable

     def showValue(self):
         self.c=self.a*self.a
         print(self.c)

     def showValue1(self,a,b):
         c = a + b  # here we can user argument variable without self
         print(c)

obj= Demo()
obj.sum()
obj.showValue()
obj.showValue1(12,13)

