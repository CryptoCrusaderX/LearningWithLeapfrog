import requests

# Get- Retrieve Data
get = requests.get("https://jsonplaceholder.typicode.com/users/7")
print(get.json())

# Post- Create New Data
data = {"title": "JUNE", "body": "MONDAY", "userId": 1}

post = requests.post("https://jsonplaceholder.typicode.com/users", json=data)
print("POST:")
print(post.status_code)
print(post.json())

# PUT-Replacing Entire Data
put_data = {"id": 777, "name": "John-doe", "address": "Kathmand,Nepal"}
put = requests.put("https://jsonplaceholder.typicode.com/users/8", json=put_data)
print("PUT:")
print(put.status_code)
print(put.json())

# Delete - Deleteting the Data
delete = requests.delete("https://jsonplaceholder.typicode.com/users/8")
print("DELETE:")
print(delete.status_code)
print(delete.raw)  # NO output

# Head- Requests req headers

head = requests.head("https://jsonplaceholder.typicode.com/users/8")
print("HEAD:")
print(head.status_code)
print(head.headers)
