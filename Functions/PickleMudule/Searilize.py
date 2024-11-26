import pickle

l=[10,20,30,40,50]

file = open("writeData.txt","wb")
pickle.dump(l,file) # store data in txt file