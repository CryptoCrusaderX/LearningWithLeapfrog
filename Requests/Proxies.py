import requests

proxies = {
    "http": "http://127.0.0.1:8000",
    "https": "https://127.0.0.1:8000",
}

response = requests.get("http://example.org", proxies=proxies)
print("Per-Request Status:", response.status_code)

session = requests.Session()
session.proxies.update(proxies)

response = session.get("http://example.org")
print("Session-Wide Status:", response.status_code)
