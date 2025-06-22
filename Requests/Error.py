import requests
import requests.exceptions

try:
    response = requests.get("https://httpbin.org/status/500", timeout=3)
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)
except requests.exceptions.Timeout:
    print("Request Timed Out!")
except requests.exceptions.ConnectionError:
    print("Network Problem!")
except requests.exceptions.RequestException as e:
    print("Something went wrong:", e)
