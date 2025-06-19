import requests

url = "https://httpbin.org/post"

response = requests.options(url)

print(response.headers.get("server"))
