import requests

try:
    r = requests.get("https://httpbin.org/delay/7", timeout=(2, 7))
except requests.exceptions.ConnectTimeout:
    print("Connection timed out!")
except requests.exceptions.ReadTimeout:
    print("Read timed out!")
