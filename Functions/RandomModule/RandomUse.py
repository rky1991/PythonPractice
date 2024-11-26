import random as r

print(r.randint(5,10)) # randome number 5-10

print(r.randrange(3,9)) # random number 3-8 , 9 will not include in it

print(r.random())

l=["apple","Bananna","grap","chiku"]
print(r.choice(l))

l1=[10,20,30,40]
r.shuffle(l1)
print(l1) # suffled element in list

print(r.uniform(5,10)) # 5-10 float value