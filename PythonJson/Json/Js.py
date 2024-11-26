import json

d =  '{"name":"John", "age":30, "city":"New York"}'

x = json.loads(d)
print(x)
print(type(x))