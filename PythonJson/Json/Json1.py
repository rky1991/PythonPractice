import json

d={
    'CourseName':'Python',
    'Fee':15000
}
f= json.dumps(d)
print(type(f))
print(f)