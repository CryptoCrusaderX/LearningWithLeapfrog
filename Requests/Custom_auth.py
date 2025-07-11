from requests.auth import AuthBase
import requests


class PizzaAuth(AuthBase):

    def __init__(self, username):
        self.username = username

    def __call__(self, r):
        r.headers["X-Pizza"] = self.username
        return r


response = requests.get("https://httpbin.org/headers", auth=PizzaAuth("Sarad"))

print(response.status_code)
