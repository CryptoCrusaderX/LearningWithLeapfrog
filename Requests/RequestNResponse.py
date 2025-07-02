import requests

r = requests.get("https://httpbin.org/get")


print("Response JSON:\n", r.json())

print("\nResponse Header:\n", r.headers)

print("\nRequests Header:\n", r.request.headers)
