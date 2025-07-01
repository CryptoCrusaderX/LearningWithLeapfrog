import requests

s = requests.Session()
s.auth = ("user", "pass")

s.headers.update({"x-test": "True"})

response = s.get("https://httpbin.org/headers", headers={"x-test2": "true"})

print(response.text)
