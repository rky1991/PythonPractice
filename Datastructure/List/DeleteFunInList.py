#del
#pop()
#remove()
#clear()

l= [1,2,3,"Rahul",23.4,'r',]
print(l)
del[l[1]] # Delete 1st index value from list
print("del use to delete index value after ",l)

#pop()--> Return value that is deleted by it

popElement=l.pop(2)
print("Pop() Element ->",popElement ,",Current List is ", l)

#remove() --> use to delete by value
l.remove('r') # will take only one argument
print("Remove() delete passed value 'r' ",l)

#clear() --> clear all elements from the list, will make it empty list

l.clear()
print("cleared complete list -->",l)