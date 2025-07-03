from requests import Request, Session

url = "https://httpbin.org/post"
data = {"msg": "hello"}
headers = {"User-Agent": "SaradTWIN/1.0"}

s = Session()

req = Request("POST", url, data=data, headers=headers)
prepped = s.prepare_request(req)

prepped.body = "Tame Impala | Kevin Parker"

settings = s.merge_environment_settings(prepped.url, {}, None, None, None)

resp = s.send(prepped, **settings)

print(resp.status_code)
print(resp.json())
