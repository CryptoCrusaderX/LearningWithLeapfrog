import requests


token_url = "https://dev-xn4ny5n8.us.auth0.com/oauth/token"
client_id = "NOQIQYt2AXiF3P7ZOk9y6CgENAX3H1R0"
client_secret = "xs0xU4rjA_5M6sM7BZH4Y0PLT9OnrJtFn6eGAnpIEvWNz"

data = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret,
    "audience": "https://dev-xn4ny5n8.us.auth0.com/api/v2/",
}

response = requests.post(token_url, json=data)

if response.status_code == 200:
    token = response.json()["access_token"]
    print("Access token:", token[:50], "...")
else:
    print("Failed:", response.status_code)
    print(response.text)
