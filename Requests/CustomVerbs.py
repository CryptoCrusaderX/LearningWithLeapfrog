import requests

url = "https://httpbin.org/anything"
response = requests.request("MKCOL", url)

print("Status Code:", response.status_code)

try:
    print("Response JSON:", response.json())
except requests.exceptions.JSONDecodeError:
    print("Response content (not JSON):", response.text)
