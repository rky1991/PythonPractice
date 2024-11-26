class ExceptionHandling:

     try:
          a = int(input("Enter First Number :"))
          b = int(input("Enter First Number : "))
          c = a / b
          print("Division =", c)

 #if Exceotion occored then only Except block will execute
     except:
          print("Divide by Zero not allowed")
     #if Try block succeffully executed then else block will execute
     else:
          print("Program Executed Successfully")
     # finally always be execute either excetion come or not
     finally:
          print("This will always be Execute")
