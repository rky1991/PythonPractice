class Area:
    def find_area(self,x=None,y=None):

        if x!=None and y!=None:
            print(x*y)
        elif x!=None:
            print(x*x)
        else:
            print("Nothing Parameter is passed")

ob= Area()
ob.find_area(10,20)
ob.find_area(10)
ob.find_area()