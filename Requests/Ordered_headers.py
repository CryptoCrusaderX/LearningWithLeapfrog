import requests
from collections import OrderedDict

session = requests.session()

session.headers = OrderedDict(
    [
        ("X-Custom-Header", "123"),
        ("User-Agent", "my-app/1.0"),
        ("Accept", "application/json"),
        ("Authorization", "Bearer exampletoken"),
    ]
)

response = session.get("https://httpbin.org/headers")

print("Request sent with these headers (order preserved):")
print(response.json())
