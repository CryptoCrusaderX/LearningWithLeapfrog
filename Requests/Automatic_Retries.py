import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()

retries = Retry(
    total=3,
    backoff_factor=0.1,
    status_forcelist=[502, 503, 504],
    allowed_methods={"GET"},
)

adapter = HTTPAdapter(max_retries=retries)
session.mount("https://", adapter)

response = session.get("https://httpbin.org/status/200")
print("Code:", response.status_code)
