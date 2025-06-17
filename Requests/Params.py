import requests

url = "https://jsonplaceholder.typicode.com/users"
params = {"users": 1}
param2 = {"id": [1, 2, 3]}
result = requests.get(url, params=params)
result2 = requests.get(url, params=param2)
print(result.url)
print(result2.url)
