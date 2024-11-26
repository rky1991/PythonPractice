import  json
file = open("jsonData.json","r")
string_data=file.read()
final_data=json.loads(string_data)
print(final_data)

print(type(final_data))

for i in final_data:
    print(i['configKey'])