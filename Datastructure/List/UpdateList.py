l=[10,2,30,40,50]
l[1]=20 # Will Replace value at index 1
print("List is updated ->",l)

#insert
#append
#extends
print(l)
l.insert(0,90) # add 90 at 0 index
print(l)

#append
l.append(70) # add value in the last
print(l)
l1=[32,43] # complete list add at last
l.append(l1)
print(l)

#extends
l.extend(l1)
print(l) # add all value in the list