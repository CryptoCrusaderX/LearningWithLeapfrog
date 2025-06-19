import requests

url = "http://example.com/some/cookie/setting/url"

r = requests.get(url)

r.cookies["cookie_name"]
cookies = dict(cookies_are="working")

r = requests.get(url, cookies=cookies)

r.text
jar = requests.cookies.RequestsCookieJar()

jar.set("tasty_cookie", "yum", domain="httpbin.org", path="/cookies")

jar.set("gross_cookie", "blech", domain="httpbin.org", path="/elsewhere")

url = "https://httpbin.org/cookies"

r = requests.get(url, cookies=jar)

r.text
