import json

d='{"CourseName":"Python","Fee":15000,"Duration:"2 Month"}'

x = json.loads(d)
print(x)