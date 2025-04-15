import json

new_data = {"name": "Alice", "age": 25, "city": "New York"}

with open('C:\PythonWorkspace\Python_Practice\PythonJson\jsonFiles\data.json', 'w') as file:
    json.dump(new_data, file, indent=4)