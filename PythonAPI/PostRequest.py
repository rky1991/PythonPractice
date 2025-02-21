# API Endpoint
import requests

url = "https://jsonplaceholder.typicode.com/posts"

# Data to send
data = {
    "title": "Hello API",
    "body": "This is a sample request",
    "userId": 1
}

# Sending POST request
response = requests.post(url, json=data)

# Print response
print("Status Code:", response.status_code)
print("Response Data:", response.json())
