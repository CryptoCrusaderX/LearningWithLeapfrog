import requests

r = requests.head("http://github.com/", allow_redirects=True)

print(r.url)

print(r.status_code)

print(r.history)
