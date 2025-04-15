jsonData = {
    "data": {
        "id": 2,
        "email": "janet.weaver@reqres.in",
        "first_name": "Janet",
        "last_name": "Weaver"
    }
}

# Use str() function
print("id IS --> " + str(jsonData['data']['id']))

#Option 2: Use f-string (recommended)
print(f"id is --> {jsonData['data']['id']}")

#Option 3: Use , in print (automatically handles types)
print("id is -->", jsonData['data']['id'])