import requests

proxies = {
    "http": "socks5h://127.0.0.1:9050",  # Use socks5h to resolve DNS via proxy
    "https": "socks5h://127.0.0.1:9050",
}

try:
    response = requests.get("http://httpbin.org/ip", proxies=proxies, timeout=10)
    print("Your IP via proxy:", response.json())
except requests.exceptions.RequestException as e:
    print("Proxy request failed:", e)
