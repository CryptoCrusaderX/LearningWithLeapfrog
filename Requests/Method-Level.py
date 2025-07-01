import requests

s = requests.Session()

r = s.get("https://httpbin.org/cookies", cookies={"Sarad": "Kandel"})
print(r.text)


r = s.get("https://httpbin.org/cookies")
print(r.text)
