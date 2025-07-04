import requests

url = "https://self-signed.badssl.com/"

try:
    requests.get(url)
except requests.exceptions.SSLError as e:
    print("SSL ERROR:", e)

response = requests.get(url, verify=False)

print("Status: ", response.status_code)
