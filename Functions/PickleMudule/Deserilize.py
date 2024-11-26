import pickle

f= open("writeData.txt","rb")
data=pickle.load(f)
print(data)