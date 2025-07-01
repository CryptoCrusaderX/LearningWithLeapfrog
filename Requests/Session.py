import requests

s = requests.Session()

s.get("https://httpbin.org/cookies/set/sessioncookie/Sarad-Kandel")
r = s.get("https://httpbin.org/cookies")

print(r.text)

print(s.headers)
print(s.auth)
