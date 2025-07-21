import ssl
from urllib3.poolmanager import PoolManager
from requests.adapters import HTTPAdapter
import requests


class SecureTLSAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False, **kwargs):
        self.poolmanager = PoolManager(
            num_pools=connections,
            maxsize=maxsize,
            block=block,
            ssl_version=ssl.PROTOCOL_TLS_CLIENT,  # Safer and supported
        )


session = requests.Session()
session.mount("https://", SecureTLSAdapter())

response = session.get("https://httpbin.org/get")
print("Status Code:", response.status_code)
