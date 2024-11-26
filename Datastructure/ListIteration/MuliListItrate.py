l=[10,20,30,40]
l1=[33,22,44,55]

for a,b in zip(l,l1): # l value go in a variable and l1 values in b
    print(a,b)

l2=[31,21,41,51,61]
for a,b in zip(l,l1): # l and l2 are not same in index , zip() ignore 61
    print(a,b)