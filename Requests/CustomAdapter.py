import requests
from requests.adapters import BaseAdapter
from requests.models import Response
from urllib.parse import urlparse
import io


class PrintOnlyAdapter(BaseAdapter):
    def send(
        self, request, stream=False, timeout=None, verify=True, cert=None, proxies=None
    ):
        print(f"[Adapter] Intercepted request to :{request.url}")

        response = Response()
        response.status_code = 200
        response._contnet = b"This is a fake response generated from PrintOnlyAdapter"
        response.url = request.url
        response.request = request

        return response

    def close(self):
        pass


session = requests.Session()

session.mount("http://fake.local/", PrintOnlyAdapter())

response = session.get("http://fake.local/test")
print("Response Status Code:", response.status_code)
print("Reponse Text:", response.text)

response2 = session.get("https://httpbin.org/get")
print("Real request status code:", response2.status_code)
