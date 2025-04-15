import  json

file = open("C:\PythonWorkspace\Python_Practice\PythonJson\jsonFiles\jsonData.json", "r")

# Read file
string_data=file.read()
#Load json data
final_data=json.loads(string_data)

print("Json File Data -->>",final_data)
print(final_data.configKey)


print(type(final_data))
