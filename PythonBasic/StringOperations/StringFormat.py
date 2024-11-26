#format()
#placeholder -->{}

#using Varivale placeholder
s="My first name is {fname} and last name is {lname}"

print(s.format(fname="Rahul",lname="Yadav"))

#using index placeholder
w="My first name is {0} and last name is {1}"

print(w.format("Rahul","Yadav"))

#using empty placeholder
x="My first name is {} and last name is {}"

print(x.format("Rahul","Yadav"))

#using empty placeholder
x="My first name is {a:10} and last name is {b}"

print(x.format(a=2,b=25))  # number 10 will create 10 char white space

#using empty placeholder 10 in center
x="My first name is {a:^10} and last name is {b}"

print(x.format(a=21,b=25))  # ^ take 10 in middle will create 10 char white space

#using empty placeholder -- right
x="My first name is {a:>10} and last name is {b}"

print(x.format(a=21,b=25))  # ^ take 10 in middle will create 10 char white space

#using empty placeholder --->>left
x="My first name is {a:<10} and last name is {b}"

print(x.format(a=21,b=25))  # ^ take 10 in middle will create 10 char white space