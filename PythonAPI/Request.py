import requests

# API Endpoint
url = "https://jsonplaceholder.typicode.com/posts/1"

# Sending GET request
response = requests.get(url)

# Print response data
print("Status Code:", response.status_code)  # 200 means success
print("Response Data:", response.json())  # Convert to JSON

print("*************************************************")
# Get the Response ------>>>>>>>>>>>>>>>>>>>>>>>
response = requests.get("https://jsonplaceholder.typicode.com/invalid-url")

if response.status_code == 200:
    print("Success:", response.json())
else:
    print(f"Error {response.status_code}: {response.text}")

