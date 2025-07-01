import requests
from requests.cookies import RequestsCookieJar

s = requests.Session()
jar = RequestsCookieJar()
jar.set("Kathmandu", "Nepal")
s.cookies = jar
print(s.cookies)
