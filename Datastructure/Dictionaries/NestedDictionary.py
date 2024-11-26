# Nested dictionaly
#dictionary under another dictionary
#EX:

course={
    'php':{'Duration':'2 month','Fees':15000},
    'Python':{'Duration':'3 month','Fees':18000},
     'Java':{'Duration':'4 month','Fees':20000}


}

print(course)

#get data
print(course['php']['Fees'])

for key,value in course.items():
    print(key,value['Duration'],value['Fees'])

#Update
course['Python']['Fees']=20000
print(course)