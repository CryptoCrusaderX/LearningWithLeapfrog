import requests

r = requests.get("https://jsonplaceholder.typicode.com/users/1")

print(r.text)
print("\nContent:")

print(r.content)
print("\nHeader:")
print(r.headers)

print(r.status_code)
print(r.json())
