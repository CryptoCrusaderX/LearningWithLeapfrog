from requests_oauthlib import OAuth1
import requests

# Dummy OAuth1 credentials for testing with Postman Echo
consumer_key = "postman"
consumer_secret = "postman"
access_token = "postman-access-token"
access_token_secret = "postman-access-token-secret"

# Setup OAuth1
auth = OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)

# Make a test request to Postman Echo
url = "https://postman-echo.com/oauth1"
response = requests.get(url, auth=auth)

# Display results
print("Status Code:", response.status_code)
print("Response Body:", response.text)
