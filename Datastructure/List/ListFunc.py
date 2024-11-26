#count()
#max()
#min()
#sort()
#reverse()
#index()

l=[10,20,30,40,50,10,30,30]
#count() -->find the repeted values
print(l.count(10))
n=l.count(30)
print(n)
#max()
m=max(l)
print(m) # max value in the list
#min()
m=min(l)
print(m) # min value in the list

#sort()
l.sort()
print(l) # sorted list

#reverse()
l.reverse()
print(l)

#index()
n=l.index(40) # print index of 40
print(n)