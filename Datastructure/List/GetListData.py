l= [1,2,3,"Rahul",23.4,'r',]
print(l)

print(l[2]) #3
print(l[3]) #"Rahul"
print(l[2],l[5]) #3 ,r

print("size of list ",l.__len__()) # size of


#Slicing of List ------>>>>>>>.
print(l[0:2]) # [1,2]
print(l[0::2]) # [1, 3, 23.4] , increment by 2

print(l[3:]) # ['Rahul', 23.4, 'r']

#Reverse -->
print(l[-1::-1]) # ['r', 23.4, 'Rahul', 3, 2, 1]

print(l[-1::-2]) # ['r', 'Rahul', 2]