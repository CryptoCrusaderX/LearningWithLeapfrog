import requests

url = "https://httpbin.org/post"

files = {"file": open("myfile.txt", "rb")}

data = {"username": "sarad"}

response = requests.post(url, files=files, data=data)

print(response.status_code)
print(response.json())
