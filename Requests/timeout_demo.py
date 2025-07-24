import requests
from requests.exceptions import ConnectTimeout, ReadTimeout, Timeout


try:
    print("Trying to connect to a non-routable IP (connect timeout = 3s)...")
    response = requests.get("http://10.255.255.1", timeout=(3, 10))
except ConnectTimeout:
    print("ConnectTimeout: Failed to establish a connection within 3 seconds.")
except Timeout:
    print("General Timeout Exception.")


try:
    print("\nTrying to get a delayed response from httpbin.org (read timeout = 2s)...")
    response = requests.get("https://httpbin.org/delay/5", timeout=(3, 2))
except ReadTimeout:
    print("ReadTimeout: Server took too long to send data.")
except Timeout:
    print("General Timeout Exception.")
else:
    print("Success:", response.status_code)
