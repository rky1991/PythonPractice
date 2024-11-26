#Immutable in Nture - can not change value of it.

t=(10,20,30,40,50)
size=len(t)
print(type(t))
#get
for i in range(size):
    print(t[i])
print("------------------->>>>>>>>>>")
for i in t:
    print(i)


t1=(10)
print(type(t1)) # not tuple -> Int