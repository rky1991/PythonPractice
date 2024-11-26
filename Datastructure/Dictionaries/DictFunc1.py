#get()
#keys()
#values()
#items()

d={
    'EmpName':'Rahul',
    'EmpId':2502552,
    'Department':'Engineering',
    'Address':'B-73,Gzb'
}

#get() --->>>Get values based on keys
value=d.get('EmpName','EmpId')
print(value)
value=d.get('EmpId')
print(value)

#keys() -->> Will return all keys
k=d.keys()
print(k) #o/p-->(['EmpName', 'EmpId', 'Department', 'Address'])

#value() --> will return all value
print(d.values()) #dict_values(['Rahul', 2502552, 'Engineering', 'B-73,Gzb'])

#items()
for i , j in d.items():
    print(i,j)

# EmpName Rahul
# EmpId 2502552
# Department Engineering
# Address B-73,Gzb