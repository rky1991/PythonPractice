from types import SimpleNamespace

jsonData = {
    "data": {
        "id": 2,
        "email": "janet.weaver@reqres.in",
        "first_name": "Janet",
        "last_name": "Weaver"
    }
}

# Use dot notation

dataElements=jsonData['data']
jsonObject=SimpleNamespace(**dataElements)
print("Id is -->",jsonObject.id)
print("Email Is -->",jsonObject.email)
